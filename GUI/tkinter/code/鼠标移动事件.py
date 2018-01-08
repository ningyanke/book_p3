#!/usr/bin/evn python
# codign=utf-8

"""
鼠标移动事件
"""
import tkinter as tk

root = tk.Tk()


def _printCoords(events):
    print(events.x, events.y)

# 创建第一个 BUTTON ,并与左键移动事件绑定

bt1 = tk.Button(root, text="left button")
bt1.bind("<B1-Motion>", _printCoords)

# 鼠标右键移动事件绑定
bt2 = tk.Button(root, text="right button")
bt2.bind("<B3-Motion>", _printCoords)

# 鼠标中间移动事件绑定
bt3 = tk.Button(root, text='middle butotn')
bt3.bind("<B2-Motion>", _printCoords)

bt1.grid()
bt2.grid()
bt3.grid()

tk.mainloop()
