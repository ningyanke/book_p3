#!/usr/bin/env python
# coding=utf-8

"""[demo5]
[显示Message控件]
"""

from tkinter import *


root = Tk()
root.title("demo5")
whatever_you_do = "I wanne go to China"

msg = Message(root, text=whatever_you_do)
msg.config(bg='lightgreen', font=("微软雅黑", 24))
msg.pack()

mainloop()
