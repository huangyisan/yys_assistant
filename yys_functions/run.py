import keyboard
import time

def on_triggered():
    print("Triggered!")
    while True:
        if keyboard.is_pressed('ctrl+w'):
            time.sleep(1)
            print(1111)
on_triggered()