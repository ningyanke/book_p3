#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:ning
@file:面向对象.py
@time:12/27/20178:27 AM
"""
from math import pi, sin, cos, radians


def inputinfo():
    angle = eval(input("Enter the launch angle(in degrees):"))
    vel = eval(input("Enter the initial velocity(in meters/sec)"))
    h0 = eval(input("Enter the initial height (in meters):"))
    time = eval(input("Enter the time interval:"))

    xpos = 0
    ypos = h0

    theta = radians(angle)
    xvel = vel * cos(theta)
    yvel = vel * sin(theta)

    while ypos >= 0:
        xpos = xpos + time * xvel
        yvel1 = yvel - time * 9.8
        ypos = ypos + time * (yvel + yvel1) / 2.0
        yvel = yvel1
    print("\n Distance traveled:{0:0.1f} meters".format(xpos))


if __name__ == '__main__':
    inputinfo()
