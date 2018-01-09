#!/usr/bin/env python
# coding=utf-8

import multiprocessing
import time


def foo1(i):
    time.sleep(2)
    return i + 100


def bar(arg):
    return arg


if __name__ == '__main__':
    res_list = []
    t_start = time.time()
    pool = multiprocessing.Pool(5)
    for i in range(10):
        # 使用了关键字 func
        # func的结果(return) 成为了回调函数的出入参数
        res = pool.apply_async(func=foo1, args=(i,), callback=bar)
        res_list.append(res)

    # 关闭进程池
    pool.close()

    # 阻塞直到进程池中的进程全部结束
    pool.join()
    # 输出得到的结果
    for res in res_list:
        print(res.get())
    t_end = time.time()
    print('the program time is {}'.format(t_end - t_start))
