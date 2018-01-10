#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ningyanke
# @Date:   2018-01-11 02:09:40
# @Last Modified by:   ningyanke
# @Last Modified time: 2018-01-11 02:23:17


"""
得到了tag值,也就得到了这个item,可以对这个item进行相关的设置
"""

from tkinter import *
root = Tk()

# 创建一个Canvas,设置其背景色为白色
canvas = Canvas(root, bg='white')
canvas.pack()

# 使用tags指定一个tag('r1')
rt = canvas.create_rectangle(10, 10, 110, 110, tags=('r1', 'r2', 'r3'))
canvas.create_rectangle(20, 20, 80, 80, tags='r3')
# 将所有与tags('r3') 绑定的item 边框颜色设置为蓝色
for item in canvas.find_withtag('r3'):
    canvas.itemconfig(item, outline='blue')
mainloop()
# 动态修改与tag('r3')绑定的item边框颜色
