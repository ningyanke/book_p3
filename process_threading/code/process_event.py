#!/usr/bin/env python
# coding=utf-8

import multiprocessing
import time

"""
Event 用来进程之间通信
"""


def wait_for_event(e):
    print('wait_for_event starting')
    e.wait()     # wait 会阻塞进程,直到 set 方法设置为true
    print('wait_for_event:e.is_set()->' + str(e.is_set()))


def wait_for_event_timeout(e, t):
    print("wait_for_event_timeout:starting")
    e.wait(t)
    print('wait_for_event_timeout:e.is_set->' + str(e.is_set()))


if __name__ == '__main__':
    e = multiprocessing.Event()
    w1 = multiprocessing.Process(
        name='block', target=wait_for_event, args=(e,))
    w2 = multiprocessing.Process(
        name='non-block', target=wait_for_event_timeout, args=(e, 2))
    w1.start()
    w2.start()
    time.sleep(3)
    e.set()
    print('main:event is set')
