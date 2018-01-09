#!/usr/bin/env python
# coding=utf-8

import multiprocessing
import time
import random

"""
queue队列
进程间的队列
进程间是相互独立的,数据的交互可以使用队列的方式,一个进行写入,一个进行读取
"""


def writer_proc(q):
    for i in ['A', 'B', 'C', 'D']:
        print('put %s to queue....' % i)
        q.put(i)
        time.sleep(random.random())


def read_proc(q):
    while True:
        if not q.empty():
            value = q.get()
            print("Get %s from queue" % value)
            time.sleep(random.random())
        else:
            break

if __name__ == '__main__':
    # 父进程创建Queue,并传递给子进程
    qe = multiprocessing.Queue()
    pw = multiprocessing.Process(target=writer_proc, args=(qe,))
    pr = multiprocessing.Process(target=read_proc, args=(qe,))
    pw.start()
    pw.join()  # 手动阻塞,让信息先写入到队列中
    pr.start()
    pr.join()
    print("\n 所有数据都写入并且读完")
