#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
采用解堵塞的方式,让进程正常的流转,以适应更多的客户端来连接服务器
"""

from socket import *


def main():
    # 1.create socket
    sersocket = socket(AF_INET, SOCK_STREAM)
    # 2.bind
    ipaddr = ('', 8899)
    sersocket.bind(ipaddr)
    # 3.listen
    sersocket.listen(10)
    # 4.not block
    sersocket.setblocking(False)
    # 如果是服务端主动关闭的连接,允许服务端再次运行程序
    # sersocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    # 6.创建newsocket解堵塞后的保存对象
    inputs = []

    while True:
        # 5.服务端接受客户端连接
        # socket 解堵塞,如果没有客户端连接,会造成输出错误信息,因此,适应try来处理错误
        try:
            newsocket, cliaddr = sersocket.accept()
        except Exception as e:
            #  print(e)  # 测试
            pass
        else:
            # newsocket 解堵塞
            newsocket.setblocking(False)
            # 解堵塞后,newsocket对应不会阻塞等待 recv 接受数据,这样会造成客户端数据无法接受,
            # 需要生成新的列表来保存解堵塞的newsocket对象
            # 7.将对象保存到列表对象中
            inputs.append((newsocket, cliaddr))

        # 8.遍历所有的newsocket对象,如果有接受数据,就输出
        for sock, addr in inputs:
            # 由于这些newsocket是解堵塞的,所以遍历的时候,如果没有数据,则会抛出一个错误
            try:
                msg = sock.recv(1024)
                if msg:
                    print('{}:{}'.format(addr, msg.decode(encoding='utf-8')))
                # 没有数据,说明客户端主动断开了连接,调用了 close
                else:
                    # 移除关闭的连接
                    inputs.remove((sock, addr))
                    sock.close()
            except Exception as e:
                pass


if __name__ == '__main__':
    main()
