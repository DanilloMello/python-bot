from pyautogui import *
import pyautogui
import keyboard
import random
from pynput.keyboard import Listener, Key
from classes import RepeatebleTimer

def health(times):
    pic = pyautogui.screenshot(region=(0,0,960,505))
    pixel = pic.getpixel((213,47))
    if pixel[1] != 255:
        keyboard.press_and_release('1')
def spell(times, gFixo):
    pic = pyautogui.screenshot(region=(0,0,960,505))
    pixel = pic.getpixel((226,452))
    if gFixo == pixel[1]:
        keyboard.press_and_release('r')
def food(times):
    pic = pyautogui.screenshot(region=(0,0,960,505))
    pixel = pic.getpixel((473,466))
    if 117 == pixel[1]:
        keyboard.press_and_release('4')

timers = []

def start():
    rt1 = RepeatebleTimer(120 + random.randint(0, 9), food, [0])
    pic = pyautogui.screenshot(region=(0,0,960,505))
    pixel = pic.getpixel((226,452))
    rt2 = RepeatebleTimer(60 + random.randint(0, 9), spell, [0, pixel[1]])
    rt3 = RepeatebleTimer(6 + random.randint(0, 9), health, [0])
    timers.extend([rt1, rt2, rt3])

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