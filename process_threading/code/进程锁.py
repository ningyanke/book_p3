#!/usr/bin/env python
# coding=utf-8

"""
进程锁的用法和线程锁的用法相似:
线程是共享内存,共享主线程中的全局变量的.

而对于进程来讲,他们是分开独立的,共享的资源可以来自文件,可以来自队列中
多进程有很多共享资源的方法,应该尽量避免加锁

"""


import multiprocessing
import sys


def worker_with(lock, f):
    # 上下文管理器,是可以简写的
    # 等同于加锁
    with lock, open(f, 'a+') as fs:
        for i in range(10):
            fs.write('locked acquired via with: \n')


def worker_no_with(lock, f):
    lock.acquire()
    try:
        with open(f, 'a+') as fs:
            for i in range(10):
                fs.write("Lock acquired  directory\n")
    except Exception as e:
        pass
    finally:
        lock.release()

if __name__ == '__main__':
    lock = multiprocessing.Lock()
    f = 'file.txt'
    w = multiprocessing.Process(target=worker_with, args=(lock, f))
    nw = multiprocessing.Process(target=worker_no_with, args=(lock, f))
    w.start()
    nw.start()
    print('end')
