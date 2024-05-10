import sys
import os
# Import base libraries

parent_dir = os.path.abspath(os.path.dirname(__file__))
library_dir = os.path.join(parent_dir, 'libraries')
sys.path.append(library_dir)
os.system("title Crosfield Karaoke")
# Set the location of the external libraries and set the terminal title

from rich import print
from rich.layout import Layout
from rich.panel import Panel
# Import external libraries

layout = Layout()
bgcolor = "pale_turquoise1 on blue3"
highlightcolor = "pale_turquoise1 on red3"
blank = ""
paneltitle = "Blank"
# Set some style variables used by rich

side_art = """
    ░▒▓██████▓▒░░▒▓███████▓▒░ ░▒▓██████▓▒░ ░▒▓███████▓▒░         
    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░     
    ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░     
    ░▒▓█▓▒░      ░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░
    ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░
    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░
     ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓███████▓▒░
           X                   X                   X
          # #                 # #                 # #
         X   X               X   X               X   X
        #     #             #     #             #     #
       X       X           X       X           X       X
      #         #         #         #         #         #
     X           X       X           X       X           X
    #             #     #             #     #             #
   X               X   X               X   X               X
  #                 # #                 # #                 #
 X                   X                   X                   X
 ░▒▓████████▓▒░▒▓█▓▒░▒▓████████▓▒░▒▓█▓▒░      ░▒▓███████▓▒░  
░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓██████▓▒░ ░▒▓█▓▒░▒▓██████▓▒░ ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░▒▓████████▓▒░▒▓████████▓▒░▒▓███████▓▒░
""" # ASCII art that go on the left and right panels

# Set up the area panels that the content will go in using rich as well as the style of them
layout.split_column(
    Layout(name = "blank"),
    Layout(name = "header", size = 3),
    Layout(name="queuespace", size = 28),
    Layout(name="textbox", size = 12),
)

layout["header"].split_row(
    Layout(name="leftspace"),
    Layout(name="helpbar", size = 33),
    Layout(name="rightspace")
)

layout["queuespace"].split_row(
    Layout(name="queueleft"),
    Layout(name="queue"),
    Layout(name="queueright")
)

layout["queueleft"].update(
    Layout(Panel(side_art, style = "blink deep_pink4"))
)

layout["queueright"].update(
    Layout(Panel(side_art, style = "blink slate_blue1", safe_box=True))
)

layout["leftspace"].update(
    blank
)

layout["helpbar"].update(
    Layout(Panel("Type 'help' to list commands!", style = "on black" ))
)

layout["queue"].update(
    Layout(Panel("The queue is: ", style="on navy_blue"))
)

layout["rightspace"].update(
    blank
)

layout["blank"].update(
    blank
)
# Use the Rich library to define the areas of the terminal output to be that of the UI's design.


def updateArea(area, input, style, render):
    """
    updateLayout is the main front-end function in the project for setting what data is in a segment of the rendered
    screen on the console. It does this by taking the following parameters and updating the panel set with the correct
    information and whether to highlight it or to render the output.

    :param area: Which render-able area of the output to target with the update.
    :param input: Data that will be displayed in the area selected by the area parameter.
    :param style: Allows the function call to be supplied with data that will define the style of the Panel.
    :param render: Boolean input that defines whether to render the whole output.
    """
    boxvalue = str(input)
    paneltitle = "Crosfield Karaoke"
    panelstyle = "on black"
    blink = ""
    # Initial setting of the variables for the panel that will be updated at the end of the function.
    if area == "queue":
        panelstyle = "on navy_blue"
    else:
        paneltitle = ""

    if style:
        panelstyle = style
    layout[area].update(  # Update the selected area with the title, content, and style that the formatting required.
        Layout(Panel(boxvalue, title = paneltitle, style = panelstyle, border_style = blink))
    )
    if render:
        print(layout)  # If the function call specifies to render the screen again then it will be printed.
