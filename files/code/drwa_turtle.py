#!/usr/bin/env python
# -*- coding: utf-8 -*-

import turtle

"""
程序IPO
I  输入文件中的坐标值
P  turtle按照文件中的坐标值操作
O  输出图形

自顶向下设计
"""


class Draw_with_Turtle:

    def __init__(self, color):
        self.pen = turtle.Turtle()
        self.color = color
        pass

    def forward(self, ptx, *color):
        turtle.setup(800, 600, 0, 0)
        self.pen.pensize(5)
        self.pen.down()
        self.pen.color(*color)
        self.pen.speed(5)
        self.pen.forward(ptx)

    def turn(self, dirction, angle):
        if dirction == 0:
            self.pen.left(angle)
        else:
            self.pen.right(angle)


class File_for_Turtle(Draw_with_Turtle):

    def __init__(self, text, color):
        self.text = open(text, 'r')
        super(File_for_Turtle, self).__init__(color)

    def file_option(self):
        result = []
        for line in self.text:
            result.append(list(map(float, line.split(","))))

        for i in result:
            a1, a2, a3, a4, a5, a6 = i
            self.forward(a1, (a4, a5, a6))
            self.turn(a2, a3)
        turtle.mainloop()

    def file_close():
        return self.text.close()


if __name__ == "__main__":
    file1 = File_for_Turtle("./data.txt", "red")
    file1.file_option()
    file1.file_close()
