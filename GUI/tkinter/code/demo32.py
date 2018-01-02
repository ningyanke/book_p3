#!/usr/bin/env python
#coding=utf-8

# demo31
from tkinter import *

root = Tk() 
text = Text(root, width=10, height=4)

# 创建一个TAG其前景色为红色
text.tag_config('a', foreground='red')
# 创建一个TAG其前景色为蓝色
text.tag_config('b', foreground='blue')
#
# text.insert(END, 'This is a test text', ('a','b'))
#使用tag_lower来降低b的级别
text.tag_lower('b')
# 文本的颜色不是按照insert给定的顺序来设置，而是按照tag的创建顺序来设置的
# 使用'a'的颜色
text.insert(END, 'This is a test text', ('b','a'))
text.pack()


mainloop()
