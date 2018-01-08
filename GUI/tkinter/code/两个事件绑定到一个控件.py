#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ningyanke
# @Date:   2018-01-05 01:38:53
# @Last Modified by:   chanafanghua
# @Last Modified time: 2018-01-08 23:17:52

from tkinter import *
root = Tk()
# 为顶层窗口绑定2个事件

# Key 事件处理函数


def printEvent(event):
    print('<key>', event.keycode)


# Return 事件处理函数

def printReturn(event):
    print('<Return>', event.keycode)


root.bind('<Key>', printEvent)
root.bind('<Return>', printReturn)

mainloop()

# Return键是键盘上小键盘下的回车键
# 当按键为Return时,由printReturn来处理,即由最近的那个事件处理
