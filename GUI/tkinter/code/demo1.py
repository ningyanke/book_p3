#!/usr/bin/env python
# coding = utf-8

"""
demo1.py
用于显示一个Label控件的显示信息

"""

from tkinter import *

root = Tk()      # 创建顶层画布
root.title("demo1.py")
label1 = Label(root, text="Hello World")
label1.pack()    # 控制管理器
mainloop()       # 循环出现
