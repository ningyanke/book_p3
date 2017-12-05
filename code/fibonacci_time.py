#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:ning
@file:fib_time.py
@time:12/5/20172:05 PM
"""
import time


def fib1(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:

        return fib1(n - 1) + fib1(n - 2)


memo = {0: 0, 1: 1}


def fib2(n):
    if not n in memo:
        memo[n] = fib2(n - 1) + fib2(n - 2)

    return memo[n]


def fib3(n, a=0, b=1):
    if n == 0:
        return a
    return fib3(n - 1, b, a + b)


def fib_time(func, x):
    start_time = time.time()
    func(300)
    end_time = time.time()
    print("{},用时{}us".format(x, (end_time - start_time) * 1000000))


if __name__ == '__main__':
    fib_time(fib1, '普通递归')
    fib_time(fib2, '字典递归')
    fib_time(fib3, '尾递归')
