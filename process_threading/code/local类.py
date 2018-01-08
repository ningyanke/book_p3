#!/usr/bin/env python
# coding=utf-8

import threading

# 创建一个全局的local 对象
local = threading.local()


def func(var):
    local.tname = var

    print(local.tname)

if __name__ == '__main__':
    t1 = threading.Thread(target=func, args=('test1',))
    t2 = threading.Thread(target=func, args=('test2',))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
"""
local 虽然是一个全局变量, 但是确实一个 threading.local() 对象
所以,每个线程对应的局部变量是不相同的,内部保存为一个字典
"""
