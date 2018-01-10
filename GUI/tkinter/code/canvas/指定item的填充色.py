#!/usr/bin/env python
# coding=utf-8


# 创建一个矩形,指定画布的颜色为变色
# 使用属性fill设置它的填充颜色

from tkinter import *
root = Tk()
# 创建一个Canvas,设置其背景色为白色
cv = Canvas()
# 创建一个矩形,颜色为红色
cv.create_rectangle(10, 10, 110, 110, fill='red')
cv.pack()
mainloop()
