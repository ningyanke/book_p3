#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: chanafanghua
# @Date:   2018-01-08 23:24:38
# @Last Modified by:   chanafanghua
# @Last Modified time: 2018-01-08 23:28:00


from tkinter import *

root = Tk()


def printProtocol():
    print('WM_DELETE_WINDOW')
    root.destroy()

# 使用protocol将WM_DELETE_WINDOWN与printProtocol绑定
root.protocol('WM_DELETE_WINDOW', printProtocol)
# 程序在退出时打印wm_DELETE_WINDOW
mainloop()
