#!/usr/bin/env python
# coding=utf-8
# author:ning


"""
创建udpsocket客户端
"""

from socket import *


# 创建socket
# 发送和接收数据
# 关闭socket

def main():
    cliudp = socket(AF_INET, SOCK_DGRAM)  # udp socket
    ip = '10.115.28.33'
    port = 8899
    ip_port = (ip, port)
    bufsize = 1024
    cliudp.sendto(b"hello world", ip_port)  # 发送的是一个元组
    msg = cliudp.recvfrom(bufsize)
    msg1, msg2 = msg  # 返回的是一个元组,包括返回的信息和服务器的ip port
    print(msg1)
    print(msg2)
    cliudp.close()


if __name__ == "__main__":
    main()
