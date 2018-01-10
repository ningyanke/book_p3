#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ningyanke
# @Date:   2018-01-09 01:24:29
# @Last Modified by:   ningyanke
# @Last Modified time: 2018-01-09 01:44:57

from tkinter import *
root = Tk()
cv = Canvas(root, height=400, width=400, bg='white')
# x1, y1, xn, yn
cv.create_line(200, 0, 200, 400, fill='red')
cv.create_line(0, 200, 400, 200, fill='red')
cv.create_rectangle(100, 100, 300, 300, fill='green', stipple='gray12')
cv.pack()

mainloop()
