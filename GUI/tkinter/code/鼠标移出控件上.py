# 1/usr/bin/evn  python
# coding=utf-8

"""

鼠标离开控件 事件
"""

from tkinter import *
root = Tk()


def printCoords(event):
    print(event.x, event.y)

# 定义一个Button,并且与leave 事件联系

bt1 = Button(root, text='left button')
bt1.bind('<Leave>', printCoords)
bt1.pack()

mainloop()
