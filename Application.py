import Constants as c
import tkinter as tk
from win32api import GetSystemMetrics as wm

from pyautogui import RIGHT

class Application(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        
        self.presets(self.parent)

        self.buttonDone = self.button(self.windowFrame, "Done", self.windowFrame.quit)
        self.buttonDone.pack(padx=10, pady=10)

        self.buttonDone = self.button(self.windowFrame, "Done", self.windowFrame.quit)
        self.buttonDone.pack(padx=10, pady=10)        

        self.presetFrame = tk.Frame(self.parent)
        self.executionFrame = tk.Frame(self.parent)

    def presets(self, parent):
        windowsPresetsImg = [
            (tk.PhotoImage(file="C:\Trabalho\Dev\Projetos Teste\python-learning\python-bot\windows_presets_01.png"), self.presetsConfig(c.WINDOW_HALF_SIZE)), 
            (tk.PhotoImage(file="C:\Trabalho\Dev\Projetos Teste\python-learning\python-bot\windows_presets_02.png"), self.presetsConfig(c.WINDOW_ONE_THIRD_SIZE))
        ]        

        self.windowFrame = self.frame(parent)
        for img, fn in windowsPresetsImg:
            self.radioButton = tk.Radiobutton(
                image= img,
                command= fn
            )
        self.windowFrame.pack(padx=20, pady=20)

    def presetsConfig(windowSize):
        ## discover the resolution screen
        screenResolution = wm(0), wm(1)
        if all(screenResolution == c.FULL_HD_RESOLUTION):
            print("TESTE")

    def button(self, frame, title, action):
        button = tk.Button(frame) 
        button["text"] = title
        button["font"] = (c.FONTS_DEFAULT_FAMILY, c.FONTS_DEFAULT_SIZE)
        button["width"] = 10
        button["command"] = action
        return button
    
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

