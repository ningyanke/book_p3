#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""

text 显示多行文本,
"""

from tkinter import *

root = Tk()
t = Text(root,
         height=2,  # 设置高度为2个字符
         width=30  # 设置宽度为30个字符
         )
t.pack()

mainloop()
