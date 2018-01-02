#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""[demo24]

[设置起始值 from_ 
终止值 to
刻度 tickinterval
步长 resolution
]
"""


from tkinter import *

root = Tk()
# 起始值,终止值
scale1 = Scale(root, from_=0, to=50, tickinterval=10)
scale1.pack()
# 设置 刻度显示
scale2 = Scale(root, from_=0, to=60, orient=HORIZONTAL, tickinterval=2)
scale2.pack()

scale3 = Scale(root, from_=0, to=60, orient=HORIZONTAL, tickinterval=2, length=800)
scale3.pack()


# 设置步距
scale4 = Scale(root, from_=0, to=60, orient=HORIZONTAL, tickinterval=10, length=800, resolution=10)
scale4.pack()
mainloop()