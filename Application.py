import Constants as Const
import tkinter as Tk

from pyautogui import RIGHT

class Application(Tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        Tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.windowFrame = Tk.Frame(self.parent, highlightcolor="gray", highlightthickness=5)
        self.windowFrame.pack(padx=20, pady=20)

        self.buttonDone = self.button(self.windowFrame, "Done", self.windowFrame.quit)
        self.buttonDone.pack(side=RIGHT)
        

        self.presetFrame = Tk.Frame(self.parent)
        self.executionFrame = Tk.Frame(self.parent)


    def button(self, frame, title, action):
        button = Tk.Button(frame)
        button["text"] = title
        button["font"] = (Const.FONTS_DEFAULT_FAMILY, Const.FONTS_DEFAULT_SIZE)
        button["width"] = 5
        button["command"] = action
        return button
        

if __name__ == "__main__":
    root = Tk.Tk()
    Application(root).pack(side="top", fill="both", expand=True)
    root.mainloop()

