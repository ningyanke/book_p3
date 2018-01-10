#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: chanafanghua
# @Date:   2018-01-11 04:42:57
# @Last Modified by:   chanafanghua
# @Last Modified time: 2018-01-11 04:49:10

from tkinter import *
root = Tk()


canvas_width = 500
canvas_height = 150


def paint(event):
    python_green = "#476042"
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    w.create_oval(x1, y1, x2, y2, fill=python_green)

root.title("用椭圆作画")
w = Canvas(root, width=canvas_width, height=canvas_height)
w.pack(expand=YES, fill=BOTH)
w.bind('<B1-Motion>', paint)

mainloop()
