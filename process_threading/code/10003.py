#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: chanafanghua
# @Date:   2018-01-08 01:29:54
# @Last Modified by:   chanafanghua
# @Last Modified time: 2018-01-08 01:38:24

import threading
import time

num = 0

# 创建锁定池
mutex = threading.Lock()


class MyThread(threading.Thread):

    def __init__(self):
        super(MyThread, self).__init__()

    def run(self):
        global num
        time.sleep(1)
        # 获取锁
        if mutex.acquire(1):  # 设置了超时时间
            num += 1
            msg = "{} set num to {}".format(self.name, num)
            print(msg)
            mutex.acquire()   # 单一线程重复获取锁,锁没有释放,变成死锁
            mutex.release()
            mutex.release()


def main():
    for i in range(5):
        t = MyThread()
        t.start()


if __name__ == '__main__':
    main()
