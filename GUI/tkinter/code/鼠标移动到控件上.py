#!/usr/bin/evn python
# codinbg=utf-8

"""
确定(Enter)事件
鼠标移动到其他控件上的事件,与之对应的是鼠标移出控件产生的事件
"""

# 只有在第一次进入产生事件,在组件中移动不会产生事件
from tkinter import *

root = Tk()


def printCoords(event):
    print(event.x, event.y)

# 创建第一个button,然后将他和Enter事件绑定
Bt1 = Button(root, text="leftmost button")
Bt1.bind('<Enter>', printCoords)
Bt1.pack()

mainloop()
