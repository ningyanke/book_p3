#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from functools import reduce

root = Tk()


list2 = [0, 0]
list1 = ["0", "0"]
list3 = ["0"]


class AppButton:
    global list1, list2, list3

    def __init__(self, valure):
        self.btn = Button(root, text=str(valure), command=self.saytext)
        self.btn.pack()

    def saytext(self):
        # self.getbtn()
        # print(self.btn["text"])

        if self.btn["text"] != "+" and self.btn["text"] != "=":
            list1.append(self.btn["text"])
            # print(list1)  # 测试程序

        elif self.btn["text"] == "+":
            str_1 = "".join(list1)
            # list2.append(reduce(lambda x, y: x + y, str_1))
            list2.append(str_1)
            list1.clear()
            # print(list2)

        elif self.btn["text"] == '=':
            str_3 = "".join(list1)
            list2.append(str_3)
            str2 = [int(i) for i in list2]
            num = reduce(lambda x, y: x + y, str2)
            list3.append(num)
            list1.clear()
            list2.clear()
            # print(list3,list2,list1)

    def getbtn(self):
        self.btn.pack()


test2 = StringVar()
test2.set("test")
label = Label(root, textvariable=test2)
label.pack()

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "+", "="]


def ppint_end():
    return test2.set(list3[-1])


for i in a:
    if i != "=" and i != "+":
        AppButton(i).getbtn()

    elif i == "+":
        AppButton(i).getbtn()

    elif i == "=":
        AppButton(i).getbtn()
        Button(root, text="确认输出结果", command=ppint_end).pack()


mainloop()
