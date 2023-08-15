from re import search
import time
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
HEALTH_PIXEL = 75
HEALTH_POSITION = [161,56] 
SPELL_POSITION = [237,385]

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

def getSpellPixels(spp):
    y = 0
    pixels = []
    for ps in spp:        
        ss = pyautogui.screenshot(region= (ps[0],y,ps[2],ps[3]))
        g = ss.getpixel((SPELL_POSITION[0],SPELL_POSITION[1]))
        pixels.append(g[1])
        y =+ ps[3]
    return pixels

def getHealthPixels(spp):
    y = 0
    pixels = []
    for ps in spp:        
        ss = pyautogui.screenshot(region= (ps[0],y,ps[2],ps[3]))
        g = ss.getpixel((HEALTH_POSITION[0],HEALTH_POSITION[1]))
        pixels.append(g[1])
        y =+ ps[3]
    return pixels

def getWindowSizeByResolution():
    screenWidth = GetSystemMetrics(0)
    screenHeight = GetSystemMetrics(1)
    resolution = []
    if screenWidth == 1920 and screenHeight == 1080:
        resolution.extend([583,509])
    return resolution
    
def health(times, wspp):
    for i in range(len(wspp[0])):
        w = wspp[0][i]
        pixelTarget = getHealthPixels(wspp[1])
        if pixelTarget[i] in range(70,80):
           ActivateWindow(w)
           keyboard.press_and_release('1')
        time.sleep(random.randint(0,2))
            
def spell(times, wspp):
    pixelsSource = getSpellPixels(wspp[1])
    for i in range(len(wspp[0])):
        w = wspp[0][i]
        pixelTarget = getSpellPixels(wspp[1])
        if pixelTarget[i] in pixelsSource:
           ActivateWindow(w)
           keyboard.press_and_release('r')
        time.sleep(random.randint(0,5))

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
    wspp = getWindowsSizeAndPosition()
    rt = RepeatebleTimer(120 + random.randint(0, 9), food, [0, wspp])
    rt2 = RepeatebleTimer(60 + random.randint(0, 5), spell, [0, wspp])
    rt3 = RepeatebleTimer(6 + random.randint(0, 2), health, [0, wspp])
    timers.extend([rt2,rt3])

    [t.start() for t in timers]    

def stopped(key):
    print(key)
    if Key.alt_gr== key:
        [t.cancel() for t in timers]
        return False

def manager():
    start()

manager()

with Listener(on_press= stopped) as listener:
    listener.join()