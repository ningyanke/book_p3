#!/usr/bin/env python
# coding=utf-8

import multiprocessing
import time
import os
import random

# 写数据 进程执行的代码


def write(q):
    print('write启动{}, 父进程为{}'.format(os.getpid(), os.getppid()))
    for i in ["Python", 'C', 'Java']:
        q.put(i)


# 读数据 进程执行的代码


def read(q):
    print('read启动{}, 父进程为{}'.format(os.getpid(), os.getppid()))
    for i in range(q.qsize()):
        msg = q.get(True)
        print("取出{}".format(msg))


if __name__ == '__main__':

    # 使用manager中的Queue 来初始化
    q = multiprocessing.Manager().Queue()
    # 创建一个进程池
    po = multiprocessing.Pool()
    # 使用阻塞的方式来创建进程,这样就不需要设置死循环了,可以让witer完全执行完后
    # 在由reader去读取
    po.apply(write, (q,))
    po.apply(read, (q,))
    # close 必须在前面
    po.close()
    po.join()
    print("{} End".format(os.getpid()))
