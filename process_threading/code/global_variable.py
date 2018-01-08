#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: chanafanghua
# @Date:   2018-01-08 00:17:50
# @Last Modified by:   chanafanghua
# @Last Modified time: 2018-01-08 00:25:36

# global_variable.py

# 多线程,共享全局变量
# 一个进程中所有的线程共享全局变量,能够在不使用其他方式的前提下,完成多线程之间的数据
# 共享

import threading
import time

global_num = 100


def work1():
    global global_num
    for i in range(3):
        global_num += 1
    print("in work1, global_num is %d" % global_num)


def work2():
    global global_num
    print('in work2, global_num is %d' % global_num)


print("---线程创建之前g_num is %d----" % global_num)

t1 = threading.Thread(target=work1)
t1.start()

time.sleep(1)

t2 = threading.Thread(target=work2)
t2.start()
