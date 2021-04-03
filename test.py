from pynput import keyboard
from time import time


start = 0
end = 0

def on_press(key):
    global start
    if key == keyboard.Key.space:
        start = time()

def on_release(key):
    global start, end
    if key == keyboard.Key.space:
        end = time()
        print(f'time taken = {end-start}')
        start=0
        end=0



with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()