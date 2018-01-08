#!/usr/bin/env python
# coding=utf-8

import multiprocessing
import time
import random


class MyProcess(multiprocessing.Process):

    def __init__(self):
        super(MyProcess, self).__init__()

    def run(self):
        print("child process pid is {} , start at: {}".format(
            self.pid, time.ctime()))
        for i in range(5):
            print('hello world')
            time.sleep(random.random())
        print("end child process")

if __name__ == '__main__':
    for i in range(5):

        p = MyProcess()
        p.start()
