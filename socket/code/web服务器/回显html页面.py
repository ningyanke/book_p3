#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
web静态服务器显示固定的HTML页面的内容
"""

from socket import *
from multiprocessing import *
import re


HTML_ROOT_DIR = './html_page'


def handle_headers(status, phrease):
    response_first_line = 'HTTP/1.1 %s %s\r\n' % (status, phrease)
    response_header = b'Server:MyWebServer\r\n'
    return response_first_line.encode(encoding='utf-8') + response_header


def handle_cli(sock):
    recvmsg = sock.recv(1024).decode(encoding='utf-8')
    # show HTTP Request msg
    # print(recvmsg)

    # create HTTP response msg
    # response_first_line = b'HTTP/1.1 200 OK\r\n'
    # response_header = b'Server:MyWebServer\r\n'
    # response_body = b'This is a test for HTTP'
    # response = response_first_line + response_header + b'\r\n'
    # + response_body

    # send html page to client

    # get recvmsg first line
    request_first_line = recvmsg.split('\r\n')[0]

    # user re get filename
    patt = '\w+ (/[^ ]*)'
    filename = re.match(patt, request_first_line).group(1)

    # set index html page
    if '/' == filename:
        filename = '/index.html'
    try:
        f = open(HTML_ROOT_DIR + filename, 'rb')
    except IOError as e:   # 文件不存在
        response_header = handle_headers('404', 'Not Found')
        response_body = b'File Not found'
        response = response_header + b'\r\n' + response_body
    else:               # 文件存在
        response_header = handle_headers('200', 'OK')
        response_body = f.read()
        response = response_header + b'\r\n' + response_body

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
