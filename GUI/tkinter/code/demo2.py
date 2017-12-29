#!/usr/bin/env python
# coding=utf-8

"""
deno2.py
使用Label控件显示图片和文字
"""
from tkinter import *

root = Tk()

label1 = Label(root, text="文本信息", justify=LEFT, padx=10, pady=10)
label1.pack(side=TOP)
picture1 = PhotoImage(file="giphy.gif")
label2 = Label(root, text="图片信息", image=picture1)
label2.pack(side=BOTTOM)
picture2 = PhotoImage(file="aniri.gif")
label3 = Label(root, text="这是将要显示在图片上的文字", image=picture2,
               justify=LEFT, compound=CENTER, font=("YaHei", 20))
label3.pack(side=BOTTOM)

lable4 = Label(root, text="font color/foreground", justify=LEFT,
               font=("Time", 20), fg="red")
lable4.pack()
lable5 = Label(root, text="background", font=("Indie Flower Regular", 21),
               bg="blue")
lable5.pack()

mainloop()
