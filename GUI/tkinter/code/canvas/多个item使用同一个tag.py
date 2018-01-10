#!/usr/bin/env python
# coding=utf-8

"""
tags 对象标签,可以为对象添加标签,通过标签来控制对象的属性

"""
from tkinter import *
root = Tk()
# 创建一个Canvas,设置其 背景色为白色
canvas = Canvas(root, bg='white')
# 使用tags指定一个tag(r1)
rt = canvas.create_rectangle(10, 10, 110, 110, tags=('r1', 'r2', 'r3'))
canvas.pack()

canvas.create_rectangle(20, 20, 80, 80, tags='r3')

# find_withtag 返回所有与tag绑定的item
print(canvas.find_withtag('r3'))

mainloop()
