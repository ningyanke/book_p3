#!/usr/bin/env python
# coding=utf-8

"""[demo22]

scrollbar
"""

from tkinter import *
root = Tk()
scrollbar = Scrollbar(root)
# fill 指定填充的位置
scrollbar.pack(side=RIGHT, fill=Y)
listbox = Listbox(root)
listbox.pack(side=LEFT)
for i in range(100):
    listbox.insert(END, i)
# 绑定命令
scrollbar.config(command=listbox.yview)
listbox.config(yscrollcommand=scrollbar.set)


scrollbar1 = Scrollbar(root, orient=HORIZONTAL)
scrollbar1.pack(side=BOTTOM)
mainloop()
