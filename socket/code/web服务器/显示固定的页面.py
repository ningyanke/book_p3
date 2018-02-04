#!/usr/bin/env python
# coding=utf-8


"""
web静态服务器回显固定的页面
使用单进程服务器实现
"""


from socket import *
from multiprocessing import Process


def handle_cli(sock):
    recvmsg = sock.recv(1024)
    # show HTTP Request msg
    print(recvmsg)

    # create HTTP response msg
    response_first_line = b'HTTP/1.1 200 OK\r\n'
    response_header = b'Server:MyWebServer\r\n'
    response_body = b'This is a test for HTTP'
    response = response_first_line + response_header + b'\r\n' + response_body
    sock.send(response)
    # close socket
    sock.close()


def main():
    # create socket
    sersocket = socket(AF_INET, SOCK_STREAM)
    # bind
    ipaddr = ('', 8899)
    sersocket.bind(ipaddr)
    # listen
    sersocket.listen(20)
    # restart socket
    sersocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    # accept
    while True:
        newsocket, cliaddr = sersocket.accept()
        print('From {}:{} connection'.format(cliaddr[0], cliaddr[1]))
        p1 = Process(target=handle_cli, args=((newsocket,)))
        p1.start()
        # main process close socket, child process start socket
        newsocket.close()


if __name__ == '__main__':
    main()
