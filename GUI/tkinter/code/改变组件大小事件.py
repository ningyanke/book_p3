#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ningyanke
# @Date:   2018-01-05 01:28:53
# @Last Modified by:   chanafanghua
# @Last Modified time: 2018-01-08 23:16:54


from tkinter import *

root = Tk()

# 处理改变控件大小的事件


def printSize(event):
    print(event.width, event.height)

root.bind('<Configure>', printSize)

mainloop()

# 当组件的大小改变时触发, event.width/height 分别触发宽和高
