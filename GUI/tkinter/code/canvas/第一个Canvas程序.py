#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ningyanke
# @Date:   2018-01-09 00:08:35
# @Last Modified by:   ningyanke
# @Last Modified time: 2018-01-09 00:09:43

# 指定画布的颜色为白色
from tkinter import *

root = Tk()
# 为了明显起见,可以设置为红色,明显的区别与root
cv = Canvas(root, bg='red')
cv.pack()
mainloop()
