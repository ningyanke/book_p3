#!/usr/bin/env python
# coding=utf-8

import threading
import random
import time

class MyThread(threading.Thread):


    def __init__(self):
        super(MyThread, self).__init__()


    def run(self):
        wait_time = random.randint(1, 10)
        print('{} will wait {} seconds'.format(self.name, wait_time))
        time.sleep(wait_time)
        print('{} finished !'.format(self.name))


if __name__ == '__main__':
    print('main thread is waitting for exit...')
    for i in range(5):
        t = MyThread()
        t.setDaemon(True)
        t.start()
    print("main thread finished!")
