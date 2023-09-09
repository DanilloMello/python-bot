from threading import Timer
from tkinter import *
import constants as Const

class Application():
    def __init__(self, master:None) -> None:
        self.windowFrame = Frame(master)
        self.windowFrame.pack(side=RIGHT)

        self.buttonDone = self.button(self.windowFrame, "Done", self.windowFrame.quit)
        self.buttonDone.pack(side=RIGHT)

        self.buttonDone = self.button(self.windowFrame, "Done1", self.windowFrame.quit)
        self.buttonDone.pack()

        self.spellFrame = Frame(master)
        self.healthManaFrame = Frame(master)
        self.spotFrame = Frame(master)

    def button(self, frame, title, action):
        button = Button(frame)
        button["text"] = title
        button["font"] = (Const.FONTS_DEFAULT_FAMILY, Const.FONTS_DEFAULT_SIZE)
        button["width"] = 5
        button["command"] = action
        return button

class RepeatebleTimer(Timer):
    def run(self):
        print(self.args)
        if (self.args[0] == 0):
            self.function(*self.args,**self.kwargs)
            while not self.finished.wait(self.interval):  
                self.function(*self.args,**self.kwargs)  
        else:
            i = 1
            self.function(*self.args,**self.kwargs)
            while not self.finished.wait(self.interval) & i != self.args :
                self.function(*self.args,**self.kwargs)
                i += 1

