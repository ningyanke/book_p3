#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:ning
@file:面向对象.py
@time:12/27/20178:50 AM
"""
from math import sin, cos, radians


class Projectile:
    def __init__(self, angle, velocity, height):
        # 根据给定的发射角度,初始速度和位置创建一个投射体对象
        self.xpos = 0.0
        self.ypos = height
        theta = radians(angle)
        self.xvel = velocity * cos(theta)
        self.yvel = velocity * sin(theta)

    def update(self, time):
        # 更新投射体状态
        self.xpos = self.xpos + time * self.xvel
        yvel1 = self.yvel - 9.8 * time
        self.ypos = self.ypos + time * (self.yvel + yvel1) / 2.0
        self.yvel = yvel1

    def getY(self):
        # 返回投射体的角度
        return self.ypos

    def getx(self):
        # 返回投射体的距离
        return self.xpos


# 引入对象,程序的模块化

def getIntut():
    a = eval(input("Enter the launch angle(in degrees):"))
    v = eval(input("Enter the initial velocity(in meters/sec)"))
    h = eval(input("Enter the initial height (in meters):"))
    t = eval(input("Enter the time interval:"))
    return a, v, h, t


def main():
    angle, vel, h0, time = getIntut()
    shot = Projectile()
    while shot.getY() >= 0:
        shot.update(time)
    print("\n Distance traveled:{0:0.1f}meters".format(shot.getX()))


if __name__ == '__main__':
    main()
