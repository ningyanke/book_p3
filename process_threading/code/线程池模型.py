#!/usr/bin/env python
# coding=utf-8
"""
利用队列的特性,结合线程池操作
"""

from queue import Queue
import time
import threading


# 创建队列实例,用于存储任务
my_queue = Queue()


# 定义需要线程池执行的任务

def foo():
    while True:
        i = my_queue.get()
        time.sleep(1)
        print('线程:{} ,从队列中取出:{}'.format(threading.current_thread().name, i))
        my_queue.task_done()  # 发送信号,表示入列任务已经完成

if __name__ == '__main__':
    # 创建3个线程的线程池
    for i in range(3):
        t = threading.Thread(target=foo)
        t.daemon = True  # 设置守护线程,主线程退出子线程也会停止
        t.start()

    # 模拟线程池 3秒后塞进10个任务到队列
    time.sleep(3)
    for i in range(10):
        my_queue.put(i)

    my_queue.join()
