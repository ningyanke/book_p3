#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
简单多线程
'''

from socket import *
from threading import *


def send(sock):
    while True:
        # 发送消息
        msg = input('<<<')
        sock.send(msg.encode(encoding='utf-8'))  # 因为已经连接,所以不用sendto
        # 主动退出,这样tcp层面去主动的4次挥手
        if msg == '':
            break


def recive(sock):
    while True:
        # 接受消息
        data = sock.recv(1024)
        if data == '':
            break
        print('>>>', data.decode(encoding='utf-8'))


def main():
    clisocket = socket(AF_INET, SOCK_STREAM)  # SOCK_STREAM TCP
    ip = '10.115.28.33'
    port = 8899
    clisocket.connect((ip, port))   # connect 会主动进行TCP3次握手
    t1 = Thread(target=send, args=(clisocket,))
    t2 = Thread(target=recive, args=(clisocket,))
    t1.start()
    t2.start()
    t1.join()

    # 关闭连接
    clisocket.close()


if __name__ == '__main__':
    main()
