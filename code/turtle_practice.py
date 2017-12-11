#!/usr/bin/env python
# coding=utf-8

"""
source activate python35
http://blog.csdn.net/zengxiantao1994/article/details/76588580
"""
import time

'''
#1.太阳花
import turtle
import time

#同时设置画笔颜色和填充颜色
turtle.color("red",'yellow')
#开始填充
turtle.begin_fill()
#
for _ in range(50):
    turtle.forward(200)
    turtle.left(170)
#填充结束
turtle.end_fill()
#启动时间循环
turtle.mainloop()
'''

#2五角星
'''
五角星是规则图形，内角和为180，所以正五角星的内角为180/5=36
正五角星的绘画需要五条边，而转的条度是相同的，顺时针旋转180-35=144
'''
'''
import turtle

turtle.pensize(5)
turtle.pencolor("yellow")
turtle.fillcolor("red")

turtle.begin_fill()

for _ in range(5):
    turtle.forward(200)
    turtle.right(144)

turtle.end_fill()

time.sleep(2)

turtle.penup()
turtle.goto(-150,-120)
turtle.color("violet")
turtle.write("Done",font=('Arial', 40, 'normal'))


turtle.mainloop()
'''


#3时钟程序


'''
自己写的程序，只能暂时绘制一个表盘
import turtle

turtle.left(90)
for i in range(360):
    if i % 6 == 0:
        if i % 30 == 0:
            n = int(i / 30)
            turtle.penup()
            turtle.forward(200)
            turtle.pendown()
            turtle.pensize(5)
            turtle.forward(20)
            turtle.penup()
            turtle.forward(20)
            turtle.write(n, font=('Arial', 15, 'normal'))
            turtle.penup()
            turtle.goto(0, 0)
            turtle.right(6)
        else:
            turtle.penup()
            turtle.forward(200)
            turtle.dot(5)
            turtle.goto(0, 0)
            turtle.right(6)

turtle.mainloop()
'''
#时钟标准程序

'''
import turtle
from datetime import *


# 抬起画笔，向前运动一段距离放下
def Skip(step):
    turtle.penup()
    turtle.forward(step)
    turtle.pendown()


def mkHand(name, length):
    # 注册Turtle形状，建立表针Turtle
    turtle.reset()
    Skip(-length * 0.1)
    # 开始记录多边形的顶点。当前的乌龟位置是多边形的第一个顶点。
    turtle.begin_poly()
    turtle.forward(length * 1.1)
    # 停止记录多边形的顶点。当前的乌龟位置是多边形的最后一个顶点。将与第一个顶点相连。
    turtle.end_poly()
    # 返回最后记录的多边形。
    handForm = turtle.get_poly()
    turtle.register_shape(name, handForm)


def Init():
    global secHand, minHand, hurHand, printer
    # 重置Turtle指向北
    turtle.mode("logo")
    # 建立三个表针Turtle并初始化
    mkHand("secHand", 135)
    mkHand("minHand", 125)
    mkHand("hurHand", 90)
    secHand = turtle.Turtle()
    secHand.shape("secHand")
    minHand = turtle.Turtle()
    minHand.shape("minHand")
    hurHand = turtle.Turtle()
    hurHand.shape("hurHand")

    for hand in secHand, minHand, hurHand:
        hand.shapesize(1, 1, 3)
        hand.speed(0)

        # 建立输出文字Turtle
    printer = turtle.Turtle()
    # 隐藏画笔的turtle形状
    printer.hideturtle()
    printer.penup()


def SetupClock(radius):
    # 建立表的外框
    turtle.reset()
    turtle.pensize(7)
    for i in range(60):
        Skip(radius)
        if i % 5 == 0:
            turtle.forward(20)
            Skip(-radius - 20)

            Skip(radius + 20)
            if i == 0:
                turtle.write(int(12), align="center", font=("Courier", 14, "bold"))
            elif i == 30:
                Skip(25)
                turtle.write(int(i / 5), align="center", font=("Courier", 14, "bold"))
                Skip(-25)
            elif (i == 25 or i == 35):
                Skip(20)
                turtle.write(int(i / 5), align="center", font=("Courier", 14, "bold"))
                Skip(-20)
            else:
                turtle.write(int(i / 5), align="center", font=("Courier", 14, "bold"))
            Skip(-radius - 20)
        else:
            turtle.dot(5)
            Skip(-radius)
        turtle.right(6)


def Week(t):
    week = ["星期一", "星期二", "星期三",
            "星期四", "星期五", "星期六", "星期日"]
    return week[t.weekday()]


def Date(t):
    y = t.year
    m = t.month
    d = t.day
    return "%s %d%d" % (y, m, d)


def Tick():
    # 绘制表针的动态显示
    t = datetime.today()
    second = t.second + t.microsecond * 0.000001
    minute = t.minute + second / 60.0
    hour = t.hour + minute / 60.0
    secHand.setheading(6 * second)
    minHand.setheading(6 * minute)
    hurHand.setheading(30 * hour)

    turtle.tracer(False)
    printer.forward(65)
    printer.write(Week(t), align="center",
                  font=("Courier", 14, "bold"))
    printer.back(130)
    printer.write(Date(t), align="center",
                  font=("Courier", 14, "bold"))
    printer.home()
    turtle.tracer(True)

    # 100ms后继续调用tick
    turtle.ontimer(Tick, 100)


def main():
    # 打开/关闭龟动画，并为更新图纸设置延迟。
    turtle.tracer(False)
    Init()
    SetupClock(160)
    turtle.tracer(True)
    Tick()
    turtle.mainloop()


if __name__ == "__main__":
    main()
'''

#4.绘制蟒蛇

import turtle

def drawSnake(rad, angle, len, neckrad):
  for _ in range(len):
    turtle.circle(rad, angle)
    turtle.circle(-rad, angle)
  turtle.circle(rad, angle/2)
  turtle.forward(rad/2) # 直线前进
  turtle.circle(neckrad, 180)
  turtle.forward(rad/4)

if __name__ == "__main__":
  turtle.setup(1500, 1400, 0, 0)
  turtle.pensize(30) # 画笔尺寸
  turtle.pencolor("green")
  turtle.seth(-40)  # 前进的方向
  drawSnake(70, 80, 2, 15)
  turtle.mainloop()