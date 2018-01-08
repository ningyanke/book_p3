#!/usr/bin/env python
# coding=utf-8

from tkinter import *
root = Tk()


def printCoords(event):
    print("event.char=", event.char)
    print('event.keycode', event.keycode)

# 创建第一个button,绑定 backspace

bt1 = Button(root, text="Press Backspace")
bt1.bind('<BackSpace>', printCoords)

# 创建第二个Button, 绑定 回车键

bt2 = Button(root, text='Press Enter')
bt2.bind('<Return>', printCoords)

# 创建第三个Button, 绑定 F5

bt3 = Button(root, text='Press F5')
bt3.bind('<F5>', printCoords)

# 创建第四个Button, 绑定 左 shift

bt4 = Button(root, text='Left Shift')
bt4.bind('<Shift_L>', printCoords)

# 创建第四个Button, 绑定 右 shift

bt5 = Button(root, text='Right Shift')
bt5.bind('<Shift_R>', printCoords)


# 将焦点设置到第一个button上
bt1.focus_set()

for i in [bt1, bt2, bt3, bt4, bt5]:
    i.pack()

mainloop()
