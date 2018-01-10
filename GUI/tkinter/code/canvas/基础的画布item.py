#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: chanafanghua
# @Date:   2018-01-11 03:51:25
# @Last Modified by:   chanafanghua
# @Last Modified time: 2018-01-11 04:36:41


"""
 绘制基本的canvas的item 

"""


from tkinter import *
root = Tk()
# 为了跟明显的显示Canvas和root,将其设置为白色
canvas = Canvas(root, width=800, height=300, bg='white')
canvas.pack(expand=YES, fill=BOTH)

"""
line
oval  椭圆
arc
"""
# 线段item (from_x, from_y, to_x, to_y)
canvas.create_line(100, 100, 200, 200)
canvas.create_line(100, 200, 200, 300)
for i in range(1, 20, 2):
    canvas.create_line(0, i, 50, i)

# 创建椭圆,其实是一个矩形中的圆形,确定的是矩形的对角线的两点
canvas.create_oval(10, 10, 200, 200, width=2, fill='blue')
# 创建弧度
canvas.create_arc(200, 200, 300, 100)
# 创建一个矩形
canvas.create_rectangle(200, 200, 300, 300, width=5, fill='red')
# 创建一个三角形
canvas.create_polygon(0, 0, 50, 0, 50, 50)


"""
创建图像控件等

"""
photo = PhotoImage(file='../giphy.gif')
canvas.create_image(325, 10, image=photo, anchor=NW)

widget = Label(canvas, text='Hello world', fg='white', bg='black')
widget.pack()
canvas.create_window(100, 100, window=widget)
canvas.create_text(100, 280, text="welcome")
mainloop()
