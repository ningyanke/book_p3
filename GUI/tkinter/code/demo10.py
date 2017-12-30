#!/usr/bin/env python
# coding=utf8

from tkinter import *

root = Tk()

ckbtn1 = Checkbutton(root, text="python")
ckbtn1.pack()

for i in ["python", "php", "ruby"]:
    Checkbutton(root, text=i).pack()


def callcheckbutton():
    print("callcheckbutton")


Checkbutton(root, text="click me", command=callcheckbutton).pack()


def change():
    avg.set("hello world")


avg = StringVar()
avg.set("clickme")
Checkbutton(root, textvariable=avg, command=change).pack()

# 上述的textvariable使用方法与Button的用法完全相同，
# 使用此例是为了区别Checkbutton的另外的一个属性variable,此属性与textvariable不同，
# 它是与这个控件本身绑定，Checkbutton自己有值：On和Off值，缺省状态On为1，Off为0，如

v = IntVar()
v.set(1)


def getv():
    print(v.get())


Checkbutton(root, text="variable", variable=v, command=getv).pack()

"""[summary]

[Checkbutton的值不仅仅是1或0，可以是其他类型的数值，可以通过onvalue和offvalue
属性设置Checkbutton的状态值，如下代码将On设置为'python',Off值设置为'Tkinter'，
程序的打印值将不再是0或1，而是'Tkinter’或‘python]
"""  
def getvar():
    print(var.get())

var = StringVar()
Checkbutton(root, text="on/off", variable=var, onvalue="python",
            offvalue='tkinter', command=getvar).pack()

mainloop()
