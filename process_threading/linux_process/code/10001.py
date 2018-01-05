#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: chanafanghua
# @Date:   2018-01-05 20:38:46
# @Last Modified by:   chanafanghua
# @Last Modified time: 2018-01-05 20:58:39

import sys
import os
print("进程运行的pid:", os.getpid())
print("进程父进程的pid", os.getppid())
bash = os.system("ps aux | grep {}".format(os.getppid()))
print("父进程在ubuntu中的信息", bash)
print("调用进程的实际用户uid", os.getuid())
msg1 = os.system("cat /etc/passwd | grep {}".format(os.getuid()))
print(msg1)
print("调用进程的有效用户euid", os.geteuid())
msg2 = os.system("cat /etc/passwd | grep {}".format(os.geteuid()))
print(msg2)
print("调用进程的实际用户组gid", os.getgid())
print("调用进程的有效组egid", os.getegid())
