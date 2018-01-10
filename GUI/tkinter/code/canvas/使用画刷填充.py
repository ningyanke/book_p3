#!/usr/bin/env python
# coding=utf-8


# 指定画布的背景色为白色
# 使用属性stipple

from tkinter import *
root = Tk()

# 创建一个canvas ,背景颜色为白色

cv = Canvas(root, bg='white')

# 创建一个矩形区域,边框为红色,填充为绿色,自定义画刷
cv.create_rectangle(10, 10, 110, 110,
                    outline='red',
                    fill='green',
                    stipple='gray12'   # 使用画刷
                    )
cv.pack()
mainloop()
