#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
demo3.py
验证Lable的高度和宽度, Label的文字和图片的对齐方式,
文本自己的对其方式
"""

from tkinter import *

root = Tk()
root.title("demo3.py")
for i, j in zip([5, 10, 15], ["red", 'blue', 'yellow']):
    Label(root, text="The Label", height=i,
          width=10, bg=j, padx=10, pady=10).pack()
Label(root, text="welcome to www.python.org", wraplength=80,
      justify=LEFT, anchor=W, padx=10, pady=10).pack()

Label(root, bitmap='error').pack()


mainloop()
