#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: chanafanghua
# @Date:   2018-01-08 23:08:54
# @Last Modified by:   chanafanghua
# @Last Modified time: 2018-01-08 23:10:17

from tkinter import *
# Key 用于处理所有的键盘事件

root = Tk()


def printCoords(event):
    print('event.char', event.char)
    print('event.keycode', event.keycode)

# 创建第一个button, 将它与 Key键盘绑定

bt1 = Button(root, text='Press BackSpace')
bt1.bind('<Key>', printCoords)

# 将焦点设置在第一个Button上

bt1.focus_set()

bt1.grid()

mainloop()

# 处理所有的按键事件,如果是上面的特殊将,event_char 返回为空,其他情况下为这个键的值
# 如果输入大写字母,按下Shift时,有Key的事件触发,即返回2词,一次为shift 本身,另外一次为shift+key 的实际键值
