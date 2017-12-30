#!/usr/bin/env python
# coding=utf-8

"""[demo6.py]

[Tk.Frame控件,用于容纳其他控件的控件]
"""

from tkinter import *
root = Tk()
# 以不同的颜色来区别各个Frame

for fm in ["red", "blue", "yellow", "green", "white", 'black']:
    Frame(root, height=20, width=100, bg=fm).pack()

frame1 = Frame(root)
frame1.pack()
var = StringVar()
var.set("This is a Label in Frame")
label1 = Label(frame1, textvariable=var, fg='red')
label1.pack()


def pushme():
    var.set("This is a Button")


button1 = Button(frame1, text="Push me", command=pushme)
button1.pack()


labelframe1 = LabelFrame(root, text="This is a LabelFrame")
labelframe1.pack()
label2 = Label(labelframe1, text="inside LableFrame")
label2.pack()

mainloop()
