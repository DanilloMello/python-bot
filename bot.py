from pyautogui import *
import pyautogui
import time
import keyboard
import random
from pynput.keyboard import Listener, Key
from classes import RepeatebleTimer

def health(times):
        pic = pyautogui.screenshot(region=(0,0,960,505))
        r,g,b = pic.getpixel((213,47))
        if g != 255:
            keyboard.press_and_release('1')
def spell(times):
    keyboard.press_and_release('r')

def food(times):
    keyboard.press_and_release('4')

timers = []

def start():
    rt = RepeatebleTimer(120 + random.randint(0, 9), food, [0])
    rt2 = RepeatebleTimer(60 + random.randint(0, 9), spell, [0])
    rt3 = RepeatebleTimer(6 + random.randint(0, 9), health, [0])
    timers.extend([rt, rt2, rt3])

    [t.start() for t in timers]    

def stopped(key):
    print(key)
    if Key.tab == key:
        [t.cancel() for t in timers]
        return False

def manager():
    start()

manager()

with Listener(on_press= stopped) as listener:
    listener.join()