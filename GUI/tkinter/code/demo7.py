#!/usr/bin/env python
# coding=utf-8

"""[demo7.py]

[Button控件]
"""

from tkinter import *


class MyButton:
    def __init__(self, par):
        self.name = Frame(par)
        self.name.pack()
        self.var = StringVar()

    def Button(self, text, cmd):
        Button(self.name, text=text, command=cmd).pack()
        

    def Label(self):
        self.var.set("hello world")
        label = Label(self.name, textvariable=self.var)
        label.pack()


if __name__ == "__main__":
    root = Tk()
    
    def change():
        test1.var.set("change")

    test1 = MyButton(root)
    test1.Label()
    test1.Button("change",change)

    test2 = MyButton(root)
    test2.Button("quit",root.quit)
    
    mainloop()
   
