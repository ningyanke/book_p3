#!/usr/bin/env python
# coding=utf-8

# fork 子进程
import os

print('Process {} start'.format(os.getpid()))
pid = os.fork()

if pid == 0:
    print('I am chilid Process {}, and the main Process is {}'.
          format(os.getpid(), os.getppid()))
else:
    print("Main Process {}".format(os.getpid()))

print("This is main process and child process")
