#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ningyanke
# @Date:   2018-01-08 22:21:48
# @Last Modified by:   ningyanke
# @Last Modified time: 2018-01-08 22:22:19

"""
鼠标点击事件
记录下的是事件在画布上的坐标值
: event.x ,event.y
"""
from tkinter import *

root = Tk()


def _printCoords(event):
    print(event.x, event.y)

# 鼠标左键点击
bt1 = Button(root, text="leftmoust button")
bt1.bind('<Button-1>', _printCoords)

# 鼠标中间点击
bt2 = Button(root, text="middle button")
bt1.bind('<Button-2>', _printCoords)

# 鼠标右键点击
bt3 = Button(root, text="rightmost button")
bt3.bind('<Button-3>', _printCoords)

# 鼠标双击
bt4 = Button(root, text="double click")
bt4.bind('<Double-Button-1>', _printCoords)

# 鼠标三连击
bt5 = Button(root, text="三连击")
bt5.bind('<Triple-Button-1>', _printCoords)

bt1.grid()
bt2.grid()
bt3.grid()
bt4.grid()
bt5.grid()

mainloop()
