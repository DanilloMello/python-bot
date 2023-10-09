import Constants as c
import tkinter as tk
from win32api import GetSystemMetrics as wm

from pyautogui import RIGHT

class Application(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        
        self.windowFrame = self.windowPresets(self.parent)
        self.windowFrame.pack(padx=10, pady=10)

    def windowPresets(self, parent):
        windowsPresetsImg = [
            (tk.PhotoImage(file="windows_presets_02.png"), self.presetsConfig(c.WINDOW_ONE_THIRD_SIZE))
        ]        
        self.windowFrame = self.frame(parent)
        for img, fn in windowsPresetsImg:
            self.radioButtonWindow = self.radioButton(self.windowFrame, img, fn)
            self.radioButtonWindow.pack(padx=10, pady=10)
        return self.windowFrame
            
        

    def presetsConfig(self, windowSize):
        ## discover the resolution screen
        screenResolution = []
        screenResolution.extend([wm(0), wm(1)])
        if screenResolution == c.FULL_HD_RESOLUTION:
            print("TESTE")
    
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
            resolution.extend([583,509])
        return resolution

    def button(self, frame, title, action):
        button = tk.Button(frame) 
        button["text"] = title
        button["font"] = (c.FONTS_DEFAULT_FAMILY, c.FONTS_DEFAULT_SIZE)
        button["width"] = 10
        button["command"] = action
        return button
    
    def radioButton(self, frame, img, fn):
        radioButton = tk.Radiobutton(frame) 
        radioButton["image"] = img
        radioButton["command"] = fn
        return radioButton
    
    def frame(self, parent):
        frame = tk.Frame(parent)
        frame['borderwidth'] = 2
        frame['relief'] = 'solid'
        return frame
        

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x500")
    Application(root).pack(side="top", fill="both", expand=True)
    root.mainloop()

