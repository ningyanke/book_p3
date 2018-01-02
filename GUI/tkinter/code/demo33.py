#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:ning
@file:demo20.py
@time:1/2/20187:46 AM
"""

from tkinter import *

root = Tk()
t = Text(root,
         height=2,
         width=50
         )
t.pack(side=LEFT, fill=Y)

quote = """
HAMLET: To be, or not to be--that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune
Or to take arms against a sea of troubles
And by opposing end them. To die, to sleep--
No more--and by a sleep to say we end
The heartache, and the thousand natural shocks
That flesh is heir to. 'Tis a consummation
Devoutly to be wished.
"""
t.insert(END, quote)

scrollbar1 = Scrollbar(root)
scrollbar1.pack(side=RIGHT, fill=Y)
scrollbar1.config(command=t.yview)
t.config(yscrollcommand=scrollbar1.set)