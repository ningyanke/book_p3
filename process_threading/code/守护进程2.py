#!/usr/bin/env  python
# coding=utf-8

import multiprocessing
import time


def worker(interval):
    print("work start:{0}".format(time.ctime()))
    time.sleep(interval)
    print("work end:{0}".format(time.ctime()))


if __name__ == "__main__":
    p = multiprocessing.Process(target=worker, args=(3,))
    p.daemon = True  # 必须添加到 start 前面
    p.start()
    print("end!")
