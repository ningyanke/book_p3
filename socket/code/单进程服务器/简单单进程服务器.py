#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ningyanke


"""
简单单进程服务器
    处于阻塞模式, block
"""

# create socket
# bind
# listen
# accept


from socket import *


def main():
    sersocket = socket(AF_INEt, SOCK_STREAM)

    ipaddr = ('', 8899)
    sersocket.bind(ipaddr)
    sersocket.listen(5)

    while True:
        newsocket, cliaddr = sersocket.accept()
        while True:
            msg = newsocket.recv(1024)
            if msg:
                print('{}:{}'.format(cliaddr, newsocket))
            else:
                break

    sersocket.close()


if __name__ == '__main__':
    main()
