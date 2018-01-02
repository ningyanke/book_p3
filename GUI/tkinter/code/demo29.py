#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""

text 显示多行文本,
"""

from tkinter import *

root = Tk()
t = Text(root,
         height=3,  #
         width=10  # 
         )
t.pack()
# 向Text中添加文本
# 向第一行第一列插入文本
t.insert(1.0, '123456')
# 向第一行第一列插入
t.insert(2.0, 'ABCDEFG')
 
# 向第一行第一列插入
t.insert(3.5, '3.5')

mainloop()