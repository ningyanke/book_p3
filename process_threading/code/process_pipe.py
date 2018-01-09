#!/usr/bin/env python
# coding=utf-8

"""
pipe 管道消息,
    duplex
        True: 全双工模式
        False: 单工模式
"""

import multiprocessing
import time


def proc1(pipe):
    """
    发送数据
    """
    while True:
        for i in range(10000):
            print('send: %s' % i)
            pipe.send(i)  # pipe.send 发送数据
            time.sleep(1)


def proc2(pipe):
    """
    接收数据
    """
    while True:
        print('proc2 recv:', pipe.recv())  # pipe.recv 用与接收数据
        time.sleep(1)


if __name__ == '__main__':
    pipe1, pipe2 = multiprocessing.Pipe()
    p1 = multiprocessing.Process(target=proc1, args=(pipe1, ))
    p2 = multiprocessing.Process(target=proc2, args=(pipe2, ))
    p1.start()
    p2.start()
