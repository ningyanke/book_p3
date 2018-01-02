#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
设置 数字显示的位数, 控件的长度
"""

from tkinter import *

root = Tk()
scale1 = Scale(root,
               from_=0,
               to=100,
               orient=HORIZONTAL,
               resolution=0.000001,
               digit=8,
               length=800)  # 设置控件长度
scale1.pack()

mainloop()