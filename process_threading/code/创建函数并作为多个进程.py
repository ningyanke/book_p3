#!/usr/bin/env python
# coding=utf-8

import multiprocessing
import time


def worker_1(interval):
    print('worker_1')
    time.sleep(interval)
    print('End worker_1')


def worker_2(interval):
    print('worker_2')
    time.sleep(interval)
    print('End worker_2')


def worker_3(interval):
    print('worker_3')
    time.sleep(interval)
    print('End worker_3')


if __name__ == '__main__':
    for i in [worker_1, worker_2, worker_3]:
        p = multiprocessing.Process(target=i, args=(3,))
        p.start()
        print("The number of cpu is {}".format(multiprocessing.cpu_count()))

    for p in multiprocessing.active_children():
        print('child p.name: {}, p.id: {}'.format(p.name, p.pid))

    print('End')
