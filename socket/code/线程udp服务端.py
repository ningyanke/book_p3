#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from socket import *
from threading import *


def recive(sock, bufsize):
    while True:
        msg = sock.recvfrom(bufsize)
        msg1, msg2 = msg
        print('\r>>>{}:{}:{}'.format(
            msg2, time.ctime(), msg1.decode(encoding='utf-8')))


def send(sock, ip_port):
    while True:
        msg = input("\r<<<")
        sock.sendto(msg.encode(encoding='utf-8'), ip_port)


def main():
    ip = ''
    port = 8899
    ip_port = (ip, port)
    bufsize = 1024
    sersocket = socket(AF_INET, SOCK_DGRAM)
    sersocket.bind(ip_port)

    ip1 = '10.115.28.17'
    port1 = 7788
    ip_port1 = (ip1, port1)

    threads1 = Thread(target=recive, args=(sersocket, bufsize))
    threads2 = Thread(target=send, args=(sersocket, ip_port1))
    threads1.start()
    threads2.start()
    threads1.join()
    threads2.join()


if __name__ == '__main__':
    main()
