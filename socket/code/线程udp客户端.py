#!/usr/bin/env python
# -*- coding: utf-8 -*-


from socket import *
import time
from threading import Thread


def send(sock, ip_port):
    while True:
        msg = input("\r<<<")
        sock.sendto(msg.encode(encoding='utf-8'), ip_port)


def recive(sock, bufsize):
    while True:
        msg = sock.recvfrom(bufsize)
        msg1, msg2 = msg
        print('\r>>>{}:{}:{}'.format(
            msg2, time.ctime(), msg1.decode(encoding='utf-8')))


def main():
    clisocket = socket(AF_INET, SOCK_DGRAM)
    ip = '10.115.28.33'
    port = 8899
    bufsize = 1024
    ip_port = (ip, port)

    ip1 = ""
    port1 = 7788
    ip_port1 = (ip1, port1)
    clisocket.bind(ip_port1)
    threads1 = Thread(target=send, args=(clisocket, ip_port))
    threads2 = Thread(target=recive, args=(clisocket, bufsize))
    threads1.start()
    threads2.start()
    threads1.join()
    threads2.join()

    clisocket.close()


if __name__ == '__main__':
    main()
