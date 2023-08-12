from re import search
from pyautogui import *

import keyboard
import random
import pyautogui
import win32.lib.win32con as win32con
import win32gui, win32com.client
import pythoncom

from win32api import GetSystemMetrics
from pynput.keyboard import Listener, Key
from classes import RepeatebleTimer

import win32gui

MSGBOX_TITLE = 'Mirage Realms'


def callback(hwnd, custom_list):
    custom_list.append((hwnd, win32gui.GetWindowText(hwnd)))

def getWindowsSizeAndPosition():
    windowsMatched = []
    win32gui.EnumWindows(callback, windows := [])
    for window, title in windows:
        if search(MSGBOX_TITLE, title):
            windowsMatched.append(window)  
    windowSize = getWindowSizeByResolution()
    windowsPositionAndSize = []
    windowsPositionAndSize.extend([[0,0,windowSize[0],windowSize[1]],
                                   [0,0 + windowSize[1],windowSize[0],windowSize[1]]])
    for i in range(len(windowsMatched)):
        resizeWindow(windowsMatched[i], windowsPositionAndSize[i])
    return [windowsMatched, windowsPositionAndSize]


def getWindowSizeByResolution():
    screenWidth = GetSystemMetrics(0)
    screenHeight = GetSystemMetrics(1)
    resolution = []
    if screenWidth == 1920 and screenHeight == 1080:
        resolution.extend([592,509])
    return resolution
    
def health(times, prints):
    for print in prints:      
        pixel = print.getpixel((213,47))
        if pixel[1] != 255:            
            keyboard.press_and_release('1')
            
def spell(times, windowSP):
    for i in range(len(windowSP[0])):    
        ActivateWindow(windowSP[0][i])
        pixel = pyautogui.screenshot(region= (sp[0],sp[1],sp[2],sp[3])).getpixel((219,377))
        print(pixel)
        if pixel[1] != 204:
              
            keyboard.press_and_release('r')

def resizeWindow(window, positionAndSize):
    win32gui.MoveWindow(window, positionAndSize[0], positionAndSize[1], positionAndSize[2], positionAndSize[3], True)
    

def ActivateWindow(window):
    win32gui.ShowWindow(window, win32con.SW_NORMAL)
    shell = win32com.client.Dispatch("WScript.Shell", pythoncom.CoInitialize())
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)

def food(times, prints):
    for print in prints:      
        pixel = print.getpixel((213,47))
        if pixel[1] != 255:
            keyboard.press_and_release('4')

timers = []

def start():
    windowSP = getWindowsSizeAndPosition()
    rt = RepeatebleTimer(120 + random.randint(0, 9), food, [0, windowSP])
    rt2 = RepeatebleTimer(60 + random.randint(0, 9), spell, [0, windowSP])
    rt3 = RepeatebleTimer(6 + random.randint(0, 9), health, [0, windowSP])
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