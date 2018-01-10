#!/usr/bin/env python
# coding=utf-8

# 使用属性tags 设置item 的tag
# 使用Canvas的方法gattags获取自动item的tags

from tkinter import *
root = Tk()

# 创建一个Canvas,设置背景色为白色
cv = Canvas(root, bg='white')

# 使用tags 指定一个tag('r1')
rt = cv.create_rectangle(10, 10, 110, 110, tags='r1')
cv.pack()

print(cv.gettags(rt))

# 使用tags 属性指定多个tags,即重新设置tags的属性

cv.itemconfig(rt, tags=('r2', 'r3', 'r4'))
print(cv.gettags(rt))
mainloop()
