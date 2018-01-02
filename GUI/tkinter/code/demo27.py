#!/usr/bin/env python
# -*- coding:utf-8 -*-
from tkinter import *

root = Tk()
# 设置滑块
scale1 = Scale(root,
               from_=0,  # 起始
               to=100,  # 终止
               orient=HORIZONTAL,  # 水平显示
               resolution=5,  # 步长
               tickinterval=5,  # 显示
               length=800,  # 位宽
               label="选择刻度"  # 提示信息
               )
scale1.grid(row=0)

# 设置输入框 entry
entry1 = Entry(root)
entry1.grid(row=1, column=1)

# 显示错误信息的 label
var = StringVar()
var.set(":)")
label1 = Label(root, textvariable=var)
label1.grid(row=2, column=0)

# 用于判断的 command
# 只能返回 True, False
def cmd1():
    s = entry1.get()
    if int(s) and (int(s) % 5 == 0) and (0 <= (int(s) / 5) <= 20):
        return True
    else:
        return False

# 返回 False后调用的command
def cmd2():
    var.set("输入错误")

# 输入框判断 entry 
entry1.config(validate="focusout", validatecommand=cmd1, invalidcommand=cmd2)

# 
label2 = Label(root, text="输入刻度")
label2.grid(row=1, column=0)


def cmd3():
    if cmd1():
        e = entry1.get()
        return scale1.set(int(e))


button1 = Button(root, text="显示刻度", command=cmd3)
button1.grid(row=2, column=1)

mainloop()