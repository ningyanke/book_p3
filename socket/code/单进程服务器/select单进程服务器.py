#!/usr/bin/env python
# coding=utf-8


"""
调用系统底层的select函数,提高效率
"""


from socket import *
from select import select


def main():
    # 1.create socket
    sersocket = socket(AF_INET, SOCK_STREAM)
    # 2.bind
    ipaddr = ('', 8899)
    sersocket.bind(ipaddr)
    # 3.listen
    sersocket.listen(5)

    # 5.create reacable socket list
    inputs = [sersocket]
    # 4.accept
    while True:
        # select方法接受3个常用参数,分别是接受数据,发送数据,产生错误的socket
        # select 阻塞遍历3个列表,如果有请求,就解阻塞
        readable, writeable, exceptional = select(inputs, [], [])

        # print(readable)
        # [<socket.socket fd=3, family=AddressFamily.AF_INET, \
        # type=SocketKind.SOCK_STREAM, proto=0, laddr=('0.0.0.0', 8899)>]
        # select底层是对fd,也就是文件描述符的改变的遍历

        for sock in readable:
            # sock如果是新的连接,就将sock添加到inputs列表中,接受数据
            if sock == sersocket:
                newsocket, cliaddr = sock.accept()
                inputs.append(newsocket)
            # sock如果是已添加到inputs中的客户端连接,就输出数据
            else:
                msg = sock.recv(1024)
                if msg:
                    print('{}:{}'.format(sock.getpeername(),
                                         msg.decode(encoding='utf-8')))
                else:
                    inputs.remove(sock)
                    sock.close()


if __name__ == '__main__':
    main()
