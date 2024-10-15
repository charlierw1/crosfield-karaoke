from render import updateArea
from time import sleep
from random import shuffle
# Import Libraries


class Commands:  # Class for setting commands to whatever is needed
    help = "help"
    exit = "exit"
    add = "add"
    remove = "remove"
    lock = "lockjudelol"
    next = "next"
    skip = "skip"
    shuffle = "shuffle"
    spacequeue = "spacequeue"


class Settings:  # Class for settings vars
    shuffle_amount = 2  # The minimum amount of songs needed in the queue to use the shuffle command


# GUI Variables
textbox = "textbox"
queue = "queue"
cmds = f"""
    {Commands.help} - List commands
    {Commands.add} - Add a song to the queue
    {Commands.remove} - Remove a song from the queue
    {Commands.next} - Show the next song in the queue
    {Commands.skip} - Skip a song to the front of the queue
    {Commands.shuffle} - Shuffle the current queue to be random
    {Commands.exit} - Exit the program
    {Commands.spacequeue} - Add a song to the queue after another song has been added
    """
message = "Enter a command:"

# Function Variables
songlist = []
spacequeue = []
locked = False

# Loop through operations until program is terminated via the exit command
while True:
    if len(songlist) > 0:
        queuemessage = ""
        for index, song in enumerate(songlist):
            queuemessage += f"{index + 1}: {song} \n\n"
    else:
        queuemessage = "The queue is currently empty, type 'add' to queue a song"
    # As long as there are songs in the queue, they are added to the fstring and displayed in a list

    updateArea(queue, queuemessage, False, False)
    updateArea(textbox, message, False, True)
    # Update both the queue and message box with their respective data
    command = input()
    match command.lower():
        case Commands.help:
            message = cmds

        case Commands.exit:
            break

        case Commands.add:
            if not locked:
                updateArea(textbox, "Enter the song and singer:", False, True)
                song = input()
                match song:
                    case "" | "next" | "add":  # Making sure mistakes don't get added to the queue
                        message = "Invalid song name!"
                    case other:
                        songlist.append(song)
                        message = "Song added to the queue"
                        if len(spacequeue) > 0:
                            message = f"Song added to the queue and so was {spacequeue[0]}"
                            songlist.append(spacequeue.pop(0))

            else:
                message = "The queue is currently locked and can't be altered."

        case Commands.spacequeue:
            if not locked:
                updateArea(textbox, "Enter the song and singer:", False, True)
                song = input()
                match song:
                    case  "" | "next" | "add":  # Making sure mistakes don't get added to the queue
                        message = "Invalid song name!"
                    case other:
                        spacequeue.append(song)
                        message = "Song added to the space queue"

        case Commands.remove:
            if not locked:
                if len(songlist) > 0:
                    updateArea(textbox, "Enter the number of the song to remove: ", False, True)
                    remove = input()
                    try:  # Attempt to remove selected song from the queue
                        message = f"{songlist[int(remove) - 1]} removed from the queue"
                        songlist.pop(int(remove) - 1)
                    except ValueError:
                        message = "Please enter a number in the list"
                    except IndexError:
                        message = "Number not in list"
                else:
                    message = "There are no songs in the queue to remove"
            else:
                message = "The queue is currently locked and can't be altered."

        case Commands.lock:
            if locked:
                locked = False
            else:
                locked = True
            message = f"Lock status of the queue: {locked}"

        case Commands.next:
            try:  # Try to move to the next song if it exists
                message = f"next up is {songlist[0]}"
                updateArea(textbox, message, "blink2 red", True)
                songlist.pop(0)
                sleep(4)
            except IndexError:
                message = "Queue is empty, to add something to the queue, type 'add'"

        case Commands.skip:
            if not locked:  # If the queue isn't locked move the selected song to the front of the queue
                updateArea(textbox, "Enter the number of the song to go next: ", False, True)
                skip = input()
                try:
                    message = f"{songlist[int(skip) - 1]} is now next in the queue"
                    songlist.insert(0, songlist.pop(int(skip) - 1))
                except ValueError:
                    message = "Please enter a number in the list"
                except IndexError:
                    message = "Number not in list"
            else:
                message = "The queue is currently locked and can't be altered."

        case Commands.shuffle:
            if len(songlist) >= Settings.shuffle_amount:
                shuffle(songlist)
                message = "The song list has been shuffled."
            else:
                message = f"You need at least {Settings.shuffle_amount} songs in the queue to shuffle."

        case unknown_command:
            if unknown_command == "":
                message = cmds
            else:
                message = f"'{unknown_command}' not recognised as a command, please try again"
