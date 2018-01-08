#!/usr/bin/env python
# coding=utf-8


import multiprocessing
import datetime
import time


def worker(num):
    n = 5
    while n > 0:
        print('The now is %s' % datetime.datetime.now())
        time.sleep(num)
        n -= 1

if __name__ == '__main__':
    # 实例化进程
    p = multiprocessing.Process(target=worker, args=(3,))

    # 开始进程
    p.start()

    # p.terminate()  # 强行结束一个进程
    # p.join()
    print('p.authkey', p.authkey)  # 获取进程的授权密码
    p.authkey = b'123qwe'   # 设置进程的授权密码,必须编码为ascii
    print('p.authkey', p.authkey)  # 获取进程的授权密码
    print('p.name', p.name)
    p.name = 'test'
    print('p.name', p.name)
    print('p.is_alive', p.is_alive())   # 判断进程是否存活
