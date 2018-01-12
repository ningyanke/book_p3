#!/usr/bin/env python
# coding=utf-8

"""
移动item
"""
# move指定x,y的偏移量

from tkinter import *
root = Tk()

# 创建一个cavas,设置其背景为白色

canvas = Canvas(root, bg='white')
canvas.pack()
# 创建2个同样的rectangle,比较移动前后的不同

rt1 = canvas.create_rectangle(
    10, 10, 110, 110,
    tags=('r1', 'r2', 'r3')
)

rt2 = canvas.create_rectangle(
    10, 10, 110, 110,
    tags=('r1', 'r2', 'r3')
)

# 移动rt1
canvas.move(rt1, 20, -10)

mainloop()
