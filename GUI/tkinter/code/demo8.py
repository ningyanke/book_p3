#!/usr/bin/env python
# coding=utf-8

"""[demo8]

[获取Botton上的值]
"""

from tkinter import *


class MyFrame:
    def __init__(self, desc, cmd):
        self.button = Button(root, text=desc, command=cmd)
        self.button.pack()

    def gettext(self):
        print(self.button["text"])


def say():
    print("hello myfriend")


if __name__ == "__main__":
    root = Tk()
    test1 = MyFrame("c", say)
    test2 = MyFrame("Python", test1.gettext)
    text = Text(root, height=3, width=10)
    text.pack()

    def cross(val):
        val.insert(INSERT, "X")

    test3 = MyFrame("Java", lambda: cross(text))
    mainloop()
