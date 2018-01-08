from tkinter import *

root = Tk()

# 只处理指定的按键效果


def printCoords(event):
    print("event.char", event.char)
    print('event.keycode', event.keycode)


# 创建第一个Button,并绑定 'a'
Bt1 = Button(root, text='Press')
Bt1.bind('<a>', printCoords)


# 创建第二个Button,并绑定'<'
Bt2 = Button(root, text='less than key')
Bt2.bind('<less>', printCoords)

# 创建第三个Button, 并绑定'spacebar'
Bt3 = Button(root, text='Press spacebar')
Bt3.bind('<space>', printCoords)

# 将焦点放在第一个Button上
Bt1.focus_set()

#
for i in [Bt1, Bt2, Bt3]:
    i.pack()

mainloop()
