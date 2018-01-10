#!/usr/bin/env python
# coding=utf-8

from tkinter import *


root = Tk()
# 指定画布的颜色为白色,使用 Canvas的方法来重新设置item的坐标
cv = Canvas(root, bg='white')
# 创建一个矩形,边色为红色,填充为绿色, 画刷
rt = cv.create_rectangle(10, 10, 110, 110,
                         outline='red',
                         fill='green',
                         stipple='gray12'
                         )
cv.pack()
# 重新设置rt 的坐标(相当于移动一个item)
# 动态修改item的坐标
cv.coords(40, 40, 80, 80)
mainloop()
