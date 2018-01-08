#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ningyanke
# @Date:   2018-01-05 02:00:58
# @Last Modified by:   chanafanghua
# @Last Modified time: 2018-01-08 23:21:17


"""
绑定的事件的级别之间的传递
    bind: 绑定 instance 或者 widget 或 toplevel
    bind_class: 绑定处理类函数
    bing_all: 绑定应用所有事件

事件级别间传递
"""

from tkinter import *
root = Tk()

# Key 事件处理函数


def printEvent(event):
    print('<Key>', event.keycode)


# Return 事件处理函数

def printReturn(event):
    print('<Return>', event.keycode)


def printToplevel(event):
    print('<toplevel>', event.keycode)


def printClass(event):
    print('<bind_class>', event.keycode)


def printAppAll(event):
    print('<bind_all>', event.keycode)

# 在instance级别与 printEvent 绑定
bt1 = Button(root, text='instance_class')
bt1.bind('<Key>', printEvent)

#  在bt1的toplevel级别绑定 printToplevel
bt1.winfo_toplevel().bind("<Return>", printToplevel)

# 在class级别绑定事件 printClass
root.bind_class('Button', '<Return>', printClass)

# 在application_all 级别绑定printAppAll
bt1.bind_all('<Return>', printAppAll)

# 将焦点定位在bt1上, 回车一下,结果有4个打印输出
bt1.focus_set()
bt1.pack()

mainloop()
