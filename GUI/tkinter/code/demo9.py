#!/usr/bin/evn python
# coding=utf-8

"""[demo9.py]

显示Button上relief 的浮雕效果
"""

from tkinter import *
root = Tk()

for i in ["flat", "groove", "raised", "ridge", "solid", 'sunken']:
    Button(root, text="Button", relief=i).pack()


picture1 = PhotoImage(
    file=r"E:\remote_python\book_p3\GUI\tkinter\code\aniri.gif")
label2 = Label(root, text="图片信息", image=picture1)
label2.pack()

pic1 = [PhotoImage(file=r"E:\remote_python\book_p3\GUI\tkinter\code\aniri.gif",
                   format='gif -index %i' % (i)) for i in range(100)]


def update(ind):
    frame = pic1[ind]
    ind += 1
    btn.config(image=frame)
    root.after(100, update, ind)


btn = Button(root, text="iamges", compound=CENTER)

btn.pack()
root.after(0, update, 0)


Button(root, text='botton', compound='bottom', bitmap='error').pack()
Button(root, text='top', compound='top', bitmap='error').pack()
Button(root, text='right', compound='right', bitmap='error').pack()
Button(root, text='left', compound='left', bitmap='error').pack()
Button(root, text='center', compound='center', bitmap='error').pack()


def cb1():
    print('button1 clicked')


def printEventInfo(event):
    print('event.time = ', event.time)
    print('event.type = ', event.type)
    print('event.WidgetId = ', event.widget)
    print('event.KeySymbol = ', event.keysym)


def cb3():
    print('button3 clicked')


b1 = Button(root, text='Button1', command=cb1)
b2 = Button(root, text='Button2')
b2.bind("<Enter>", printEventInfo)
b3 = Button(root, text='Button3', command=cb3)
b1.pack()
b2.pack()
b3.pack()

b2.focus_set()


mainloop()
