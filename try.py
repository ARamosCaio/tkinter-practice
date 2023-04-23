from tkinter import *
import tkinter as tk
import time
import sys


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        sentence = "Teste de escrita no tk"
        for letter in sentence :
            print(letter, end='')
            time.sleep(0.035)
            sys.stdout.flush()

root = tk.Tk()
app = Application(master=root)
app.mainloop()