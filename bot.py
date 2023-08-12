from re import search
from pyautogui import *

import keyboard
import random
import pyautogui
import win32gui

from win32api import GetSystemMetrics
from pynput.keyboard import Listener, Key
from classes import RepeatebleTimer

import win32gui

MSGBOX_TITLE = 'Mirage Realms'

def callback(hwnd, custom_list):
    custom_list.append((hwnd, win32gui.GetWindowText(hwnd)))

def getWindows():
    windowsMatched = []
    win32gui.EnumWindows(callback, windows := [])
    for window, title in windows:
        if search(MSGBOX_TITLE, title):
            windowsMatched.append(window)
    return windowsMatched


def getResolution():
    screenWidth = GetSystemMetrics(0)
    screenHeight = GetSystemMetrics(1)
    resolution = []
    if screenWidth == 1920 and screenHeight == 1080:
        resolution.extend([563,516])
    return resolution
    
def health(times, prints):
    for print in prints:      
        pixel = print.getpixel((213,47))
        if pixel[1] != 255:            
            keyboard.press_and_release('1')
            
def spell(times, windows):
    resolution = getResolution()
    widthResolution, heightResolution = 0,0
    for window in windows:
        resizeWindow(window, resolution)
        win32gui.SetForegroundWindow(window)
        ss = pyautogui.screenshot(region= (0,heightResolution,resolution[0],resolution[1]))
        heightResolution = heightResolution + resolution[1]
        if ss.getpixel[1] != 255:   
            keyboard.press_and_release('r')

def resizeWindow(window, resolution):
    y =+ resolution[1]
    x = 0
    x0, y0, x1, y1 = win32gui.GetWindowRect(window)
    w = x1 - x0
    h = y1 - y0
    win32gui.MoveWindow(window, x, y0 + y, resolution[0], resolution[1], True)

def food(times, prints):
    for print in prints:      
        pixel = print.getpixel((213,47))
        if pixel[1] != 255:
            keyboard.press_and_release('4')

timers = []

def start():
    windows = getWindows()
    print(windows)
    rt = RepeatebleTimer(120 + random.randint(0, 9), food, [0, windows])
    rt2 = RepeatebleTimer(5 + random.randint(0, 9), spell, [0, windows])
    rt3 = RepeatebleTimer(6 + random.randint(0, 9), health, [0, windows])
    timers.extend([rt2])

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