#!/usr/bin/env python
#coding=utf-8
# demo30
from tkinter import *

root = Tk()

t = Text(root)
# 向Text中添加10行文本
for i in range(1,10):
    t.insert((i+0.0),'0123456789 \n')
# 定义各个Button的回调函数，这些函数使用了内置的
# mark:INSERT/CURRENT/END (光标插入点/鼠标的当前位置所对应的字符位置/最后的一个字符位置)
def insertText():
    t.insert(INSERT,'jcodeer')
def currentText():
    t.insert(CURRENT,'jcodeer')
def endText():
    t.insert(END,'jcodeer')

#INSERT    
Button(root,
       text = 'insert jcodeer at INSERT',
       command = insertText
       ).pack(fill = X)
#CURRENT
Button(root,
       text = 'insert jcodeer at CURRENT',
       command = insertText
       ).pack(fill = X)
#END
Button(root,
       text = 'insert jcodeer at END',
       command = endText
       ).pack(fill = X)


t.pack()

mainloop() 