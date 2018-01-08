#!/usr/bin/env python
# coding=utf-8

from tkinter import *

root = Tk()

# 测试鼠标的释放事件


def printCoords(event):
    print(event.x, event.y)

# 左键释放
bt1 = Button(root, text="leftmouse button")
bt1.bind('<ButtonRelease-1>', printCoords)

# 中键释放
bt2 = Button(root, text="midlle button")
bt2.bind('<ButtonRelease-2>', printCoords)

# 右键释放
bt3 = Button(root, text="rightmouse button")
bt3.bind('<ButtonRelease-3>', printCoords)

bt1.pack()
bt2.pack()
bt3.pack()


mainloop()
