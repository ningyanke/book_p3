#!/usr/bin/env python
#coding=utf-8

# demo31
from tkinter import *

root = Tk() 
text = Text(root, width=10, height=4)

# 创建一个TAG其前景色为红色

text.tag_config('a', foreground='red')
text.insert(END, 'This is a test text', 'a')
text.pack()


mainloop()
