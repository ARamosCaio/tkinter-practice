from tkinter import *
import tkinter as tk
import time
import sys



class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.write_text()
        
    
    def write_text(self):
        self.story = tk.Label(self)
        self.story["textvariable"] = self.tell_story
        self.story.pack()

    def tell_story(self):
        print('teste de escrita simples')

root = tk.Tk()
app = App(master=root)
app.mainloop()

