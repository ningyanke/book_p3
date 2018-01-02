#!/usr/bin/env python
# coding=utf-8

"""[demo20]

[listbox]
"""

from tkinter import *

root = Tk()
frame1 = Frame(root)
frame1.pack()
listbox = Listbox(frame1)
for i in ["First", "Second", "Third"]:
    listbox.insert(END, i)

listbox.pack()

frame2= Frame(root)
frame2.pack()
frame3 = Frame(root)
frame3.pack()
frame4 = Frame(root)
frame4.pack()
frame5 = Frame(root)
frame5.pack()

listbox1 = Listbox(frame2, selectmode=BROWSE)
listbox2 = Listbox(frame3, selectmode=SINGLE)
listbox3 = Listbox(frame4, selectmode=MULTIPLE)
listbox4 = Listbox(frame5, selectmode=EXTENDED)
listbox1.pack()
listbox2.pack()
listbox3.pack()
listbox4.pack()


for i in ["First", "Second", "Third"]:
    listbox1.insert(END, i)
    listbox2.insert(END, i)
    listbox3.insert(END, i)
    listbox4.insert(END, i)

mainloop()
