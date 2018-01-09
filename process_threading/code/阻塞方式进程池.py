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
        # 这种方式是阻塞的方式,即进程会一个一个的生成,一个结束会生成另一个
        poll.apply(worker, (i,))

    print('---start-----')
    # 进程池关闭
    poll.close()
    # 等待所有的进程池中的进程执行完毕
    poll.join()
    print('---end-----')


