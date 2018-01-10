#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ningyanke
# @Date:   2018-01-11 02:23:46
# @Last Modified by:   ningyanke
# @Last Modified time: 2018-01-11 02:37:39

"""
向其他item中添加tag
使用addtag 来想上一个或者下一个item中添加tag
"""

from tkinter import *
root = Tk()
# 创建一个Canvas,设置器背景色为白色
canvas = Canvas(root, bg='white')
canvas.pack()

# 创建3个矩形框

rt1 = canvas.create_rectangle(
    10, 10, 110, 110,
    tags=('r1', 'r2', 'r3')
)

rt2 = canvas.create_rectangle(
    20, 20, 110, 110,
    tags=('s1', 's2', 's3')
)


rt3 = canvas.create_rectangle(
    30, 30, 110, 110,
    tags=('y1', 'y2', 'y3')
)

# 在rt2的上一个item添加r4
canvas.addtag_above('r4', rt2)
# 在rt2的下一个item中添加r5
canvas.addtag_below('r5', rt2)

for item in [rt1, rt2, rt3]:
    print(canvas.gettags(item))

mainloop()
# Canvas使用了stack的技术，新创建的item总是位
# 于前一个创建的item之上，故调用above时，它会
# 查找rt2上面的item为rt3,故rt3中添加了tag('r4')
# 同样add_below会查找下面的item。
