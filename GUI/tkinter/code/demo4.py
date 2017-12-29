#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
demo4.py
使用 Label.config() 来修改Label的对应值
"""

from tkinter import *
root = Tk()
root.title("demo4.py")

counter = 0


def counter_lable(var):
    def count():
        global counter
        counter += 1
        var.config(text=str(counter))
        var.after(1000, count)
    count()

test1 = Label(root, text="0")
test1.pack()
counter_lable(test1)

Button(root, text="点我停止", command=root.destroy).pack()

mainloop()
