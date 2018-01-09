#!/usr/bin/env python
# coding=utf-8

"""
进程池

"""

import multiprocessing
import time


def func(msg):
    print('msg', msg)
    time.sleep(3)
    print('end')


if __name__ == '__main__':
    pool = multiprocessing.Pool(3)
    for i in range(5):
        msg = 'hello {}'.format(i)
        """
        pool.apply_async : 　要调用的目标，　传递给目标的参数元祖
        pool.apply:
        """
        # 每次循环会用空闲的子进程去调用目标
        pool.apply_async(func, (msg,))

    print("mark,,mark,,,makr,,")
    pool.close()   # 关闭进程池
    pool.join()    # 调用join之前,先调用close(),等待所有的子进程完成
