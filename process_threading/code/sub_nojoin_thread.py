#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: chanafanghua
# @Date:   2018-01-07 20:05:20
# @Last Modified by:   chanafanghua
# @Last Modified time: 2018-01-07 20:27:34

# sub_thread.py


import threading
import time


class MyThread(threading.Thread):  # 创建线程的子类

    def __init__(self, num):
        super(MyThread, self).__init__()
        self.num = num

    def run(self):
        for i in range(5):
            time.sleep(self.num)
            msg = 'This is {}@{}'.format(self.name, i)
            print(msg)

# 生成子线程


def main():
    print("Start main thread")
    threads = [MyThread(1) for i in range(5)]   # 生成5个子线程
    for i in threads:
        i.start()
    print('End main thread')

if __name__ == '__main__':
    main()
