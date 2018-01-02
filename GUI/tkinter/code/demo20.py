#!/usr/bin/python
# coding=utf-8


"""[demo20]

[insert , delete]
"""

from tkinter import *

root = Tk()
frame1 = Frame(root)
frame1.pack()


ltb = Listbox(frame1)
ltb.pack()


ltb.insert(0, "Jack")
ltb.insert(1, "Marry")
ltb.insert(ACTIVE, "Josh")  # 插入到当前活动区域,不会按照顺序插入
ltb.insert(END, "Pork")   # 总是会插入到最后一行


# 设置一个删除按钮用于删除 listbox 中的值
frame2 = Frame(root) 
frame2.pack()

ltb1 = Listbox(frame2)
ltb1.pack()
for i in ["First", "Second", "Third"]:
    ltb1.insert(END, i)
Thebotton = Button(frame2, text="delete", command=lambda x = ltb1:x.delete(ACTIVE))
Thebotton.pack()


mainloop()
