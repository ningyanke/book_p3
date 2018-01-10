#!/usr/bin/env python
# coding=utf-8

# 创建一个item
# 创建一个矩形,指定画布的颜色为白色

from tkinter import *

root = Tk()

# 创建一个Canvas,设置其背景色为白色
cv = Canvas(root, bg='blue')

# 创建一个矩形,左边为(10,10,110,110)
cv.create_rectangle(10, 10, 110, 110)
cv.pack()
mainloop()
