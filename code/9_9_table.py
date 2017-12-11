#!/usr/bin/env python
# coding=utf-8

"""
使用conda环境管理
sourece activate python35
python3.5.4
"""
'''
实现9*9乘法表
for 循环实现
'''
for i in range(1,10):
    for j in range(1,10):
        if i >= j:
            print("{}*{}={}  ".format(j,i,j*i),end="")
    print("")  #这个是用来打印换行

'''
实现9*9乘法表
while 循环实现
'''
x = 1
while x <= 9:
    y = 1
    while y <= x:
        print("{}*{}={}  ".format(y, x, y * x), end="")
        y += 1
    print("")
    x += 1
