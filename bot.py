from pyautogui import *
import pyautogui
import keyboard
import random
from win32api import GetSystemMetrics
import pygetwindow
from pynput.keyboard import Listener, Key
from classes import RepeatebleTimer


def getResolution():
    if (GetSystemMetrics(0) == 1920 & GetSystemMetrics(1) == 1080):
        return [563,516]    
    
def presetsAndPrint():
    windows = pygetwindow.getWindowsWithTitle("Mirage Realms")
    size = getResolution()
    y = 0
    x = 0
    prints = []
    for window in windows:        
        window.activate()    
        window.resizeTo(size[0],size[1])
        y = y + size[1]
        window.moveTo(x,y)
        prints.append(pyautogui.screenshot(region=(x,y,size[0],size[1])))       
    return prints
    
def health(times, prints):
    pic = prints[0]        
    r,g,b = pic.getpixel((213,47))
    if g != 255:
        keyboard.press_and_release('1')
def spell(times, prints):
    pic = prints[0]
    pixel = pic.getpixel((213,47))
    if pixel[1] != 255:
        keyboard.press_and_release('r')

def food(times, prints):
    pic = prints[0]
    pixel = pic.getpixel((213,47))
    if pixel[1] != 255:
        keyboard.press_and_release('4')

timers = []

def start():
    prints = presetsAndPrint()    
    rt = RepeatebleTimer(120 + random.randint(0, 9), food, [0, prints])
    rt2 = RepeatebleTimer(60 + random.randint(0, 9), spell, [0, prints])
    rt3 = RepeatebleTimer(6 + random.randint(0, 9), health, [0, prints])
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