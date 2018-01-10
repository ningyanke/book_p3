#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ningyanke
# @Date:   2018-01-11 02:38:37
# @Last Modified by:   ningyanke
# @Last Modified time: 2018-01-11 02:46:31


"""
使用 find_xxx查找上一个或下一个 item
"""

from tkinter import *
root = Tk()

# 创建一个Canvas,设置器背景色为白色
canvas = Canvas(root, bg='white')
canvas.pack()
# 创建3个矩形框
rt1 = canvas.create_rectangle(
    10, 10, 110, 110,
    tags=('r1', 'r2', 'r3')
)

rt2 = canvas.create_rectangle(
    20, 20, 110, 110,
    tags=('s1', 's2', 's3')
)


rt3 = canvas.create_rectangle(
    30, 30, 110, 110,
    tags=('y1', 'y2', 'y3')
)

# 查找rt2的上一个item,并将其边框设置为空色
canvas.itemconfig(canvas.find_above(rt2), outline='red')
# 查找rt2的下一个item,并将其边框颜色设置为绿色
canvas.itemconfig(canvas.find_below(rt2), outline='green')

mainloop()
# Canvas使用了stack的技术，新创建的item总是位
# 于前一个创建的item之上，故调用above时，它会
# 查找rt2上面的item为rt3,故rt3中添加了tag('r4')
# 同样add_below会查找下面的item。
