#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ningyanke
# @Date:   2017-12-30 23:52:56
# @Last Modified by:   chanafanghua
# @Last Modified time: 2017-12-31 00:54:16

"""demo12.py 
Entity控件
"""
from tkinter import *
root = Tk()

for i in range(2):
    Label(root, text=i).grid(row=i, column=0)
    Entry(root).grid(row=i, column=1)

#L = [(3, "Firstname", "Show"), (4, "Lastname", "Quit")]
#L1 = []#
#

# def cmd():
#    print(L1)#
#

# for i, j, h in L:
#    Label(root, text=j).grid(row=i, column=0)
#    Entry(root).grid(row=i, column=1)
#    L1.append(Entry.get())
#    Button(root, text=h, command=cmd).grid(row=5, column=(i - 3))#


class MyEntry:

    def __init__(self):
        self.entry = Entry(root)

    def get(self):
        text = self.entry.get()
        return text

    def guid(self, x, y):
        return self.entry.grid(row=x, column=y)

    def label(self, name, x, y):
        label = Label(root, text=name)
        label.grid(row=x, column=y)

    def button(self, text, cmd, x, y):
        button = Button(root)
        button.config(text=text)
        button.config(command=cmd)
        button.grid(row=x, column=y)


def cmd1():
    return root.quit()


def cmd2():
    print(test1.get(), test2.get())
    # 修改调用的函数,清空内容
    test1.entry.delete(0, END)
    test2.entry.delete(0, END)

test1 = MyEntry()
test1.guid(3, 1)
test1.label("Firstname", 3, 0)

test2 = MyEntry()

test2.guid(4, 1)
test2.label("Lastname", 4, 0)
test1.button("Show", cmd2, 5, 0)
test2.button("Quit", cmd1, 5, 1)

# 插入默认值

test1.entry.insert(20, "Jack")
test2.entry.insert(20, "Ning")


mainloop()
