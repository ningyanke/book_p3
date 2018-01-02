#!/usr/bin/env python
# -*- coding:utf-8 -*-

from tkinter import *

root = Tk()

photo = PhotoImage(file="1.png")

text = Text(root, height=20, width=50)
text.insert(END, '\n')
text.image_create(END, image=photo)
text.pack(side=LEFT)

text1 = Text(root, height=20, width=50)
scroll = Scrollbar(root, command=text1.yview)
text1.config(yscrollcommand=scroll.set)
text1.tag_config('bold_italics', font=("Arial", 12, 'bold', 'italic'))
text1.tag_config('big', font=('Verdana', 20, 'bold'))
text1.tag_config('color', foreground='#476042',
                 font=('Tempus Sans ITC', 12, 'bold'))
text1.tag_bind('follow', '<1>', lambda e, t=text1: t.insert(END, "Not now, maybe later!"))
text1.insert(END, '\nWilliam Shakespeare\n', 'big')
quote = """
To be, or not to be that is the question:
Whether 'tis Nobler in the mind to suffer
The Slings and Arrows of outrageous Fortune,
Or to take Arms against a Sea of troubles,
"""
text1.insert(END, quote, 'color')
text1.insert(END, 'follow-up\n', 'follow')
text1.pack(side=LEFT, fill=Y)
scroll.pack(side=RIGHT, fill=Y)

mainloop()