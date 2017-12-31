#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
root = Tk()
L1 = [("用户名", 0), ("密码", 1)]
L2 = []

for i, j in L1:
    label = Label(root, text=i)
    label.grid(row=j, column=0)
    entry = Entry(root, show="*")
    L2.append(entry)
    entry.grid(row=j, column=1)

var = StringVar()
var.set("accept username")
label1 = Label(root, textvariable=var)
label1.grid(row=2, column=0)

var1 = StringVar()
var1.set("accept password")
label2 = Label(root, textvariable=var1)
label2.grid(row=2, column=1)


def cmd1():
    text1 = L2[1].get()
    text2 = L2[0].get()
    var.set(text2)
    var1.set(text1)


def cmd2():
    return root.quit()


Button(root, text="Show", command=cmd1).grid(row=3, column=0)
Button(root, text="Quit", command=cmd2).grid(row=3, column=1)

mainloop()
