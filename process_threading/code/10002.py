#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: chanafanghua
# @Date:   2018-01-08 00:31:46
# @Last Modified by:   chanafanghua
# @Last Modified time: 2018-01-08 01:16:50

# 10002.py

# 共享内存资源时,由于多方线程更改一个数据,造成的混乱

import threading
import time


count = 0

# 创建锁定池
lock = threading.Lock()


class MyThread(threading.Thread):

    def __init__(self):
        super(MyThread, self).__init__()

    def run(self):
        global count
        time.sleep(1)
        for i in range(1000000):
            # 上锁
            lock.acquire()
            count += 1
            # 去除锁
            lock.release()
        print("thead {} add 1000000, count is {}".format(self.name, count))


def main():
    print("Start main threading")
    for i in range(10):
        MyThread().start()

    print("End amin threading")

if __name__ == '__main__':
    main()
