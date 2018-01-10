#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ningyanke
# @Date:   2018-01-11 04:07:03
# @Last Modified by:   ningyanke
# @Last Modified time: 2018-01-11 04:23:53

from tkinter import *
root = Tk()
canvas = Canvas(root, bg='white', height=300, width=300)
canvas.pack()

# canvas.create_polygon(0, 0, 100, 100, 100, 0)
canvas.create_rectangle(0, 0, 200, 200)
canvas.create_oval(0, 0, 200, 200)
canvas.create_arc(0, 0, 200, 200, fill='blue')
canvas.create_line(0, 0, 100, 200)
canvas.create_arc(0, 0, 100, 200, fill='red')
mainloop()
