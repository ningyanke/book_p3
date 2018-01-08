#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: chanafanghua
# @Date:   2018-01-07 19:37:38
# @Last Modified by:   chanafanghua
# @Last Modified time: 2018-01-07 20:03:57

# instance_thread.py
import threading
import time


# 定义一个函数:函数是可调用对象
# 系统默认为线程创建线程名

def loop():
    print("thread %s is running...." % threading.current_thread().name)
    for i in range(5):
        print("thread %s >>> %s" % (threading.current_thread().name, i))
        time.sleep(1)

    print('thread %s ended.' % threading.current_thread().name)

if __name__ == "__main__":
    # 主线程
    print('main thread %s is running...' % threading.current_thread().name)
    # 不指定name 时,python会自动指定一个name
    t = threading.Thread(target=loop)
    t.start()
    t.join()  # 阻塞主线程,直到主线程结束
    print('main thread %s ended.' % threading.current_thread().name)
