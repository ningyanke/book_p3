#!/usr/bin/env python
# coding=utf8

from tkinter import *

root = Tk()


# 单组
# 不指定绑定变量，每个Radiobutton自成一组
Radiobutton(root, text='python').pack()
Radiobutton(root, text='tkinter').pack()
Radiobutton(root, text='widget').pack()
Checkbutton(root, text='test').pack()

# 创建一个组,创建三个Radiobutton,并绑定到整型变量v
v = IntVar()
v.set = (1)
for i in range(3):
    Radiobutton(root, variable=v, text='python', value=i).pack()

# 创建两个不同的组

vLang = IntVar()
vOS = IntVar()
vLang.set(1)
vOS.set(2)

for v in [vLang, vOS]:  # 创建两个组
    for i in range(3):  # 每个组含有3个按钮
        Radiobutton(root,
                    variable=v,
                    value=i,
                    text='python' + str(i)
                    ).pack()
mainloop()
