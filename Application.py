import Constants as Const
import tkinter as Tk

from pyautogui import RIGHT

class Application(Tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        Tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        
        self.windowFrame = self.frame(self.parent)
        self.windowFrame.pack(padx=20, pady=20)

        self.buttonDone = self.button(self.windowFrame, "Done", self.windowFrame.quit)
        self.buttonDone.pack(padx=10, pady=10)

        self.buttonDone = self.button(self.windowFrame, "Done", self.windowFrame.quit)
        self.buttonDone.pack(padx=10, pady=10)

        self.radioButtonWindows = self.radioButton(self.windowFrame)
        self.radioButtonWindows.pack(padx=10, pady=10)

        self.presetFrame = Tk.Frame(self.parent)
        self.executionFrame = Tk.Frame(self.parent)

    def radioButton(self, frame):
        radioButton = Tk.Radiobutton(frame)
        radioButton["image"] = Tk.PhotoImage(file="testando.png")
        return radioButton


    def button(self, frame, title, action):
        button = Tk.Button(frame)
        button["text"] = title
        button["font"] = (Const.FONTS_DEFAULT_FAMILY, Const.FONTS_DEFAULT_SIZE)
        button["width"] = 10
        button["command"] = action
        return button
    
    def frame(self, parent):
        frame = Tk.Frame(parent)
        frame['borderwidth'] = 2
        frame['relief'] = 'solid'
        return frame
        

if __name__ == "__main__":
    root = Tk.Tk()
    root.geometry("500x500")
    Application(root).pack(side="top", fill="both", expand=True)
    root.mainloop()

