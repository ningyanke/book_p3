#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 获取 scale 控件的值
# 使用 Scale.get 的方法来获取值

from tkinter import *

root = Tk()

scale1 = Scale(root, from_=0, to=200)
scale1.pack()
var = StringVar()
var.set("获取值")
label1 = Label(root, textvariable=var)
label1.pack()


def cmd1():
    s = scale1.get()
    return var.set(s)


button1 = Button(root, text="click", command=cmd1)
button1.pack()
mainloop()