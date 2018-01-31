#!/usr/bin/evn python
# coding=utf-8

from socket import *

# 首先创建一个socket
sersocket = socket(AF_INET, SOCK_STREAM)

# 绑定
ipaddr = ('', 8899)
sersocket.bind(ipaddr)

# listen
sersocket.listen(5)

# 非阻塞, 默认是阻塞状态,阻塞是进程的一种状态
sersocket.setblocking(False)


socket_addr = []

while True:
    # 设置非阻塞状态,如果没有客户端的连接,则会输出错误信息,try 函数处理
    try:
        newsocket, cliaddr = sersocket.accept()
    except Exception as e:
        pass
    else:
        # 设置客户端socket非阻塞
        newsocket.setblocking(False)
        socket_addr.append((newsocket, cliaddr))

    for clisocket, cliaddr in socket_addr:
        try:
            # 遍历询问,每个clisocket是否有数据,如果没有,recv默认是阻塞,非阻塞状态会输出错误
            msg = clisocket.recv(1024)
            if msg:
                print('{}:{}'.format(cliaddr, msg.decode(encoding='utf-8')))
            else:   # 客户端主动关闭连接
                socket_addr.remove((clisocket, cliaddr))
                clisocket.close()
        except Exception as e:
            pass
