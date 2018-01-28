#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
创建tcp socket server
"""

# 创建socket
# bind
# listen  侦听很重要,没有侦听,不能进行tcp的三次握手,连接会失败
# 收发消息
# 关闭连接

from socket import *


def main():
    sersocket = socket(AF_INET, SOCK_STREAM)
    ip = ''  # 表示本地的任意一张网卡都可以用来接受接收发送
    port = 8899
    sersocket.bind((ip, port))
    sersocket.listen(5)    # 调用listen,程序在TCP层面上才会处于listen状态,才会有TCP3次握手
    while True:
        newsocket, ip_port = sersocket.accept()
        while True:
            msg = newsocket.recv(1024)
            print('>>>', msg.decode(encoding='utf-8'))
            data = input('<<<')
            # 判断 data ,可以选择服务器主动的断开连接,进行TCP4此挥手过程
            if data == '':
                break

            newsocket.sendto(data.encode(encoding='utf-8'), ip_port)
        # 关闭当前连接,这样下一个可以连接,TCP4次挥手正常
        newsocket.close()

    sersocket.close()

if __name__ == '__main__':
    main()
