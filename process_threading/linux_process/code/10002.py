#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: chanafanghua
# @Date:   2018-01-05 21:12:39
# @Last Modified by:   chanafanghua
# @Last Modified time: 2018-01-05 21:18:19

import os

print("父进程开始:")
ret = os.fork()

if ret == 0:
    print("子进程开始")
    print("子进程,pid:{},ppid:{}".format(os.getpid(), os.getppid()))
    print("子进程结束")
else:
    print("父进程,pid:{}".format(os.getpid()))

print("父进程结束")
