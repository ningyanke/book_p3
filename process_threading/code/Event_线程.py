#!/usr/bin/env python
# coding=utf-8

import threading
import random
import time


class MyThread(threading.Thread):
    def __init__(self, threadName, event):
        super(MyThread, self).__init__(name=threadName)
        self.threadEvent = event

    def run(self):
        print('{} is ready !'.format(self.name))
        self.threadEvent.wait()
        print('{} run!'.format(self.name))


if __name__ == '__main__':
    sinal = threading.Event()
    for i in range(10):
        t = MyThread(str(i), sinal)
        t.start()

    sinal.set()
