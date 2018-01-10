#!/usr/bin/env python
# coding=utf-8

# 指定画布的背景色为白色
# 使用属性dash,这个值只能为奇数

from tkinter import *

root = Tk()

# 创建一个canvas ,背景色为白色

canvas = Canvas(root, bg='white')

# 创建一个矩形,填充设为green , 边框为red, dash(画虚线) 为10

canvas.create_rectangle(10, 10, 110, 110, outline='red', dash=10, fill='green')
canvas.pack()

mainloop()
