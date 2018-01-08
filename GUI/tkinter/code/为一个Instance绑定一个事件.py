#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# @Author: ningyanke
# @Date:   2018-01-05 01:51:11
# @Last Modified by:   chanafanghua
# @Last Modified time: 2018-01-08 23:19:25

# 绑定Instance的事件处理器

from tkinter import *

root = Tk()


# Key 事件处理函数,

def printEvent(event):
    print('<Key>', event.keycode)


# Return 事件处理函数


def printReturn(event):
    print('<Return>', event.keycode)

# 使用bt1 来添加一个事件处理函数

bt1 = Button(root, text='Instence event')
bt1.bind('<Key>', printEvent)
# bt1.bind('<Return>', printReturn)
bt1.focus_set()
bt1.pack()
mainloop()
