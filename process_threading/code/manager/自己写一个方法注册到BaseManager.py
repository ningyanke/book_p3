#!/usr/bin/env python
# coding=utf-8

from multiprocessing.managers import BaseManager


class MathsClass:

    def add(self, x, y):
        return x + y

    def mul(self, x, y):
        return x * y


class MyManager(BaseManager):
    pass

# 可以用于向管理器类注册类型或可调用的类方法
MyManager.register('Maths', MathsClass)

if __name__ == '__main__':
    # 实例化进程类
    manager = MyManager()
    # 为此管理器对象生成一个服务器进程
    manager.start()
    # 调用注册的方法
    maths = manager.Maths()
    print(maths.add(1, 2))
    print(maths.mul(1, 2))
