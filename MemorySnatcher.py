# Made by JACK HALES under MIT License.
# Add me on LinkedIn: https://www.linkedin.com/in/jack-h-041b32101/
# Or my website:      https://jackhales.com
# Or Facebook:        https://facebook.com/jek.hales

# Adapted by the great and mighty Oliy :sunglasses:

import pyautogui as pag
import sys, json, requests, keyboard, time

print("Waiting for you to press 'enter'")

while True:
    if keyboard.read_key() == "enter":
        print("Starting mover")
        break

def saveMem():
    # recording where the mouse first started at
    startedAt = pag.position()
    # pag.typewrite(name, interval=0.10)
    time.sleep(1)

    pag.click()

    # pag.mouseDown(button='left')

    moveDown(330)

    moveLeft(150)

    pag.click()
    time.sleep(3)

    moveDown(200)
    moveRight(130)

    pag.mouseDown(button='left')
    moveLeft(250)
    pag.mouseUp(button='left')

    moveRight(200)

    pag.click()
    time.sleep(1)

    pag.click()

    moveUp(530)

    moveRight(70)


# a few functions I wrote to make it easier to move around, since
# pyautogui new versions don't support the move function alone
def moveDown(px, time=0.5):
    now = pag.position()
    pag.moveTo(now[0], now[1]+px, time)

def moveUp(px, time=0.5):
    now = pag.position()
    pag.moveTo(now[0], now[1]-px, time)

def moveRight(px, time=0.5):
    now = pag.position()
    pag.moveTo(now[0]+px, now[1], time)

def moveLeft(px, time=0.5):
    now = pag.position()
    pag.moveTo(now[0]-px, now[1], time)

# a short-cut to refreshing from the start position on certain
# screen size
def doRefresh():
    moveUp(45, 0.2)
    moveLeft(250, 0.2)
    pag.click()
    moveRight(250, 0.2)
    pag.click()

for i in range(200):
    time.sleep(2)
    saveMem()
