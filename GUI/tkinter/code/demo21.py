#!/usr/bin/env python 
#coding=utf-8

"""[demo21]

[索引操作]
"""



from tkinter import * 
root = Tk() 

# 获取listbox 中的item的值,即索引值
# 默认Listbox只能显示前10项的值,可以通过设置, height 修改
ltb = Listbox(root, height=20)
ltb.pack()

var = StringVar()
var.set("0")
label = Label(root, textvariable=var)
label.pack()
for i in range(10):
    ltb.insert(END, i)

def cmd():
    s = ltb.size()
    var.set(str(s))
button = Button(root, text="show index number", command=cmd)
button.pack()


# 获取固定的索引值
def cmd1():
    s = ltb.get(1)
    var1.set(str(s))
var1 = StringVar()
label1 = Label(root, textvariable=var1)
label1.pack()
button1 = Button(root, text="get index 1 valure", command=cmd1)
button1.pack()

mainloop()    