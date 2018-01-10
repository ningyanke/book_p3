#!/usr/bin/env python
# coding=utf-8

# 指定画布的背景色为白色,使用属性width指定线 的宽度

from tkinter import *

root = Tk()
canvas = Canvas(root, bg='white')
# 创建一个矩形,设置背景色为红色,宽度为5,注意和canvas的宽度是不同的
# 设定矩形的边框颜色 outline 为红色
canvas.create_rectangle(10, 10, 110, 110, outline='red', width=5)
canvas.pack()
mainloop()
