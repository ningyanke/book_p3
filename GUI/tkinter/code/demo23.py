#!/usr/bin/env python
# -*- coding:utf-8 -*-

from tkinter import *

root = Tk()
scale = Scale(root, from_=0, to=50)
scale.pack()

scale1 = Scale(root, from_=0, to=200, orient=HORIZONTAL) # 定义水平方向
scale1.pack()
mainloop()