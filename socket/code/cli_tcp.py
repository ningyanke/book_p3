#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
创建tcp socket 客户端
'''

# 创建socket
# 连接服务器
# 收发信息
# 关闭连接, 关闭连接很有必要,走正常的TCP4次挥手流程

from socket import *


def main():
    clisocket = socket(AF_INET, SOCK_STREAM)  # SOCK_STREAM TCP
    ip = '10.115.28.33'
    port = 8899
    clisocket.connect((ip, port))   # connect 会主动进行TCP3次握手
    while True:
        # 发送消息
        msg = input('<<<')
        clisocket.send(msg.encode(encoding='utf-8'))  # 因为已经连接,所以不用sendto
        # 主动退出,这样tcp层面去主动的4次挥手
        if msg == '':
            break
        # 接受消息
        data = clisocket.recv(1024)
        print('>>>', data.decode(encoding='utf-8'))
    # 关闭连接
    clisocket.close()


if __name__ == '__main__':
    main()
