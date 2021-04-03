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
colorMin = 170

# center
cx = X / 2
cy = Y / 2



prevWhite = []
white = []
red = []
currRedCount = 0


spaceCount = 0

keyboard = Controller()
def pressSpace():
    global spaceCount
    keyboard.press(Key.space)
    # sleep(randrange(5500, 10000) * .00001)
    sleep(randrange(2500, 5000) * .00001)
    keyboard.release(Key.space)
    print('space', spaceCount)
    spaceCount += 1
    sleep(.5)


while True:
    # capture the center of the screen
    s = ImageGrab.grab(bbox=(cx-r, cy-r, cx+r, cy+r))
    sc = ImageOps.grayscale(s)
    loaded = sc.load()

    def changeColor(x, y, color): loaded[x,y] = color

    # loop through pixels
    for i in range(r*2):
        for j in range(r*2):

            # dounut for checking colors
            if (sqrt((r-i)**2 + (r-j)**2) > inner) and (sqrt((r-i)**2 + (r-j)**2) < r):

                # white
                if loaded[i,j] > colorMin: 
                    changeColor(i,j,255)
                    white.append((i,j))
                
                # red
                elif loaded[i,j] > 58 and loaded[i,j] < 70: 
                    changeColor(i,j,100)
                    red.append((i,j))

                else: changeColor(i,j,0)
            else: changeColor(i,j,0)


    # check to see if the color has changed
    for i in red:
        if i in prevWhite:
            currRedCount += 1

    if currRedCount > 5:
        pressSpace()
        s.show()
        sc.show()
    
    currRedCount = 0
    prevWhite = white
    red = []
    white = []

