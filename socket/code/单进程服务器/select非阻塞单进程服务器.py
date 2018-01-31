#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
select 非阻塞单进程服务器
"""

from socket import *
import select
import queue
import os


def main():
    # 1.create socket
    sersocket = socket(AF_INET, SOCK_STREAM)
    # 2.bind
    ipaddr = ('', 8899)
    sersocket.bind(ipaddr)
    # 3.listen
    sersocket.listen(5)
    # 如果服务器自己先关闭连接,可以重新连接
    sersocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    # 5 创建select3个常用的列表
    inputs = [sersocket]
    outputs = []
    # 9.创建字典存储对象,存储通信队列
    message_queues = {}
    # 6.设置超时时间,服务器可以优先关闭连接
    timeout = 20
    # 4.accept
    while True:
        print('等待连接')
        # select 3个常用参数,可以设置超时时间,服务器优先关闭连接
        readable, writeable, exceptional = select.select(
            inputs, outputs, inputs, timeout)

        # 7.如果超时,select会返回3个空列表
        if not(readable or writeable or exceptional):
            print('timeout')
            break

        # 处理接受数据
        for sock in readable:
            # 新客户端的连接
            if sock == sersocket:
                newsocket, cliaddr = sock.accept()
                print('connetction from {}'.format(cliaddr))
                # 不会阻塞等待接受数据,这样就服务端可以发送数据给客户端
                newsocket.setblocking(False)
                inputs.append(newsocket)
                # 8.设置一个字典,将socket对一个队列(queue),这样服务端可以将
                # 从客户端接收到的数据发送给客户端
                # queue 线程间的通信队列,不仅仅可以用于线程,可以用于主线程,主进程
                # 之间的通信
                message_queues[newsocket] = queue.Queue()

            # 已有客户端的处理
            else:
                msg = sock.recv(1024)
                if msg:
                    print('{}:{}'.format(sock.getpeername(),
                                         msg.decode(encoding='utf-8')))
                    # 向队列中添加数据
                    message_queues[sock].put(msg)
                    # 将socket 添加到output中,即向客户端发送数据,可以调用outputs
                    if sock not in outputs:
                        outputs.append(sock)
                else:
                    # 客户端已关闭连接
                    print('closing', sock.getpeername())
                    # 将客户端socket移出 inputs
                    inputs.remove(sock)
                    # 将客户端连接移出outputs,不在使用它发送数据
                    if sock in outputs:
                        outputs.remove(sock)
                    # 移除队列信息
                    del message_queues[sock]
                    # 服务端关闭连接
                    sock.close()

        # 服务器发送数据
        for sock in writeable:
            try:
                next_msg = message_queues[sock].get_nowait()
            except queue.Empty:
                print('{} queue empty'.format(sock.getpeername()))
                outputs.remove(sock)
            else:
                print('sending {} to {}'.format(next_msg, sock.getpeername()))
                os.popen('sleep 5').read()
                sock.send(next_msg)

        # 处理异常
        for sock in exceptional:
            print('exceptional condition on {}'.format(sock.getpeername()))

            inputs.remove(sock)
            if sock in outputs:
                outputs.remove(sock)
            sock.close()
            del message_queues[sock]


if __name__ == '__main__':
    main()
