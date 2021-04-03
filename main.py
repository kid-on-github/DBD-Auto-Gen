from time import sleep, time
from PIL import ImageGrab, Image, ImageOps
from math import sqrt
from pynput.keyboard import Key, Controller
from random import randrange

# screen dimensions 
X = 1920
Y = 1080

# radius of circle
r = 70          
inner = r-10

# color stuff and such
colorMin = 200

# center
cx = X / 2
cy = Y / 2


prevWhite = []
white = []
red = []
nowRed = 0


keyboard = Controller()
def pressSpace():
    global spaceCount
    keyboard.press(Key.space)
    sleep(randrange(2500, 5000) * .00001)
    keyboard.release(Key.space)
    sleep(.5)


while True:
    # capture the center of the screen
    orig = ImageGrab.grab(bbox=(cx-r, cy-r, cx+r, cy+r))
    loaded = orig.load()

    # loop through pixels
    for i in range(r*2):
        for j in range(r*2):

            # dounut for checking colors
            if (sqrt((r-i)**2 + (r-j)**2) > inner) and (sqrt((r-i)**2 + (r-j)**2) < r):

                a,b,c = loaded[i,j]

                # white
                if a > colorMin and b > colorMin and c > colorMin: 
                    white.append((i,j))
                
                # red
                elif a > colorMin and b < 20 and c < 20: 
                    red.append((i,j))

    # check to see if the color has changed
    for i in red:
        if i in prevWhite:
            nowRed += 1

    # if three pixels turns from white to red, press space
    if nowRed > 3:
        pressSpace()
    
    nowRed = 0
    prevWhite = white
    red = []
    white = []

