#!/usr/bin/env python
# coding=utf-8

import multiprocessing
import time
import random
import os


def worker(msg):
    t_start = time.time()
    print("{} 开始执行, 进程号为 {}".format(msg, os.getpid()))
    time.sleep(random.random())
    t_stop = time.time()
    print('{} 执行完毕,耗时{}'.format(msg, t_stop - t_start))


if __name__ == '__main__':
    # 定义一个进程池,最大为3个进程
    poll = multiprocessing.Pool(3)
    for i in range(10):
        # 这种方式是非阻塞的方式,即一下可以生成3个线程,而不是一个一个的
        poll.apply_async(worker, (i,))

    print('---start-----')
    # 进程池关闭
    poll.close()
    # 等待所有的进程池中的进程执行完毕
    poll.join()
    print('---end-----')
