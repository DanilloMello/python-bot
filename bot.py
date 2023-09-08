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

MSGBOX_TITLE = 'Mirage Realms - Early'
HEALTH_PIXEL = 75
POSITIONS_FUNCTIONS = (['spell',[237,385]], ['health',[145,57]], ['food',[214,463]])
# 145,57

def callback(hwnd, custom_list):
    custom_list.append((hwnd, win32gui.GetWindowText(hwnd)))

# TODO: REFACTORING BOT
# INTERFACE FOR ENTRIES
# ENTRIES WINDOWS SIZE -> 1 / 1 | 2 / 0 
# CHOOSE HEALTH / MANA -> PERCENTAGEM, TYPE OF POT, MAX OF SPOT 6 AND NOT REPEATEBLE SPOT 
# CHOOSE FOOD -> TYPE OF FOOD AND SPOT, MAX OF 6 AND NOT REPEATEBLE SPOT
# CHOOSE SPELL -> TYPE OF SPELL AND SPOT, MAX OF 3 AND NOT REPEATEBLE SPOT
# MODE TYPE -> TRAINING AND FIGHTING 
## TRAINING -> CHECK IF HAS TARGET WHEN TRIGGETED FOOD AND SPELL AND HEATH
## FIGHTING -> NONE FOR NOW

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

def getPixels(spp, position):
    y = 0
    pixels = []
    for ps in spp:        
        ss = pyautogui.screenshot(region= (ps[0],y,ps[2],ps[3]))
        g = ss.getpixel((position[0], position[1]))
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
    
def health(times, wspp, position):
    for i in range(len(wspp[0])):
        w = wspp[0][i]
        pixelTarget = getPixels(wspp[1], position)
        if pixelTarget[i] in range(70,95):
           ActivateWindow(w)
           keyboard.press_and_release('1')
        time.sleep(random.randint(0,2))
            
def spell(times, wspp, position):
    pixelsSource = getPixels(wspp[1], position)
    for i in range(len(wspp[0])):
        w = wspp[0][i]
        pixelTarget = getPixels(wspp[1], position)
        if pixelTarget[i] in pixelsSource:
           ActivateWindow(w)
           keyboard.press_and_release('r')
        time.sleep(random.randint(0,5))

def food(times, wspp, position):
    pixelsSource = getPixels(wspp[1], position)
    for i in range(len(wspp[0])):
        w = wspp[0][i]
        pixelTarget = getPixels(wspp[1], position)
        if pixelTarget[i] in pixelsSource:
           ActivateWindow(w)
           for i in range(4):          
            keyboard.press_and_release('4')
            time.sleep(0.7)
        time.sleep(random.randint(0,5))

def resizeWindow(window, positionAndSize):
    win32gui.MoveWindow(window, positionAndSize[0], positionAndSize[1], positionAndSize[2], positionAndSize[3], True)
    

def ActivateWindow(window):
    win32gui.ShowWindow(window, win32con.SW_NORMAL)
    shell = win32com.client.Dispatch("WScript.Shell", pythoncom.CoInitialize())
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(window)

timers = []

def filterPosition(funcao):
    for position in POSITIONS_FUNCTIONS:
        if position[0] == funcao:
            return position[1]
        
def start():
    wspp = getWindowsSizeAndPosition()
    foodThread = RepeatebleTimer(120 + random.randint(0, 9), food, [0, wspp, filterPosition("food")])
    spellThread = RepeatebleTimer(60 + random.randint(0, 5), spell, [0, wspp, filterPosition("spell")])
    healthThread = RepeatebleTimer(6 + random.randint(0, 2), health, [0, wspp, filterPosition("health")])
    timers.extend([spellThread,healthThread, foodThread])

    [t.start() for t in timers]    

def stopped(key):
    if Key.alt_gr== key:
        [t.cancel() for t in timers]
        return False

def manager():
    start()

manager()

            

with Listener(on_press= stopped) as listener:
    listener.join()