#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ningyanke
# @Date:   2018-01-05 01:07:14
# @Last Modified by:   chanafanghua
# @Last Modified time: 2018-01-08 23:14:35


from tkinter import *

root = Tk()

# 响应组合键的事件


def printCoords(event):
    print("event.char", event.char)
    print("event.keycode", event.keycode)

# 创建第一个Button, 并把它和 shift-up 绑定
bt1 = Button(root, text='Press Shift+Up')
bt1.bind('<Shift-Up>', printCoords)


# 创建第二个Button, 并绑定'control+Alt+a'
bt2 = Button(root, text='Control+Alt+a')
bt2.bind('<Control-Alt-a>', printCoords)

# 下面的键无法接受事件
# bt3 = Button(root, text='Control+Alt')
# bt3.bind('<Control-Alt>', printCoords)


for i in [bt1, bt2]:
    i.pack()

mainloop()

# 使用 Ctrl+Alt+Shift+xxx 不能单数使用前3个任意2,2组合
