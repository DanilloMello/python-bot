from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import threading

def health():
    while keyboard.is_pressed('z') == False:
        pic = pyautogui.screenshot(region=(0,0,960,505))
        r,g,b = pic.getpixel((213,47))
        if g != 255:
            keyboard.press_and_release('1')
            time.sleep(5)
def spell():
    while keyboard.is_pressed('z') == False:
        keyboard.press_and_release('r')
        time.sleep(60 + random.randint(0, 9))
def food():
    while keyboard.is_pressed('z') == False:
        keyboard.press_and_release('4')
        time.sleep(120 + random.randint(0, 9))

job1 = threading.Thread(target=health)
job2 = threading.Thread(target=spell)
job3 = threading.Thread(target=food)

job1.start()
job2.start()
job3.start()