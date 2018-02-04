#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ningyanke

"""
抽象化web服务器,将web服务器看做一个整体
"""

from socket import *
from multiprocessing import Process
import re

HTML_ROOT_DIR = './html_page'


class HTTPServer:
    '''将web服务器看做一个整体,它应该具有自己的方法和属性'''

    def __init__(self):
        # 6.实现基本的socket对象
        self.sersocket = socket(AF_INET, SOCK_STREAM)

    def bind(self, ip='', port=8899):
        # 5.实现绑定ip port, 需要有一个基本的socket对象
        self.sersocket.bind((ip, port))
        self.sersocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    def start(self, num=5):
        '''6.实现start 开启socket方法'''
        # 7.设置侦听
        self.sersocket.listen(num)
        while True:
            newsocket, cliaddr = self.sersocket.accept()
            # 8.使用子进程处理客户端socket,HTTPServer的方法之一
            p1 = Process(target=self.handle_cli, args=((newsocket,)))
            p1.start()

    def handle_cli(self, sock):
        '''9.实现handle_cli'''
        recvmsg = sock.recv(1024).decode(encoding='utf-8')

        # get recvmsg first line
        request_first_line = recvmsg.split('\r\n')[0]

        # user re get filename
        patt = '\w+ (/[^ ]*)'
        filename = re.match(patt, request_first_line).group(1)

        # handle_headers 处理response返回的数据的头部
        # set index html page
        if '/' == filename:
            filename = '/index.html'
        try:
            f = open(HTML_ROOT_DIR + filename, 'rb')
        except IOError as e:   # 文件不存在
            response_header = self.handle_headers('404', 'Not Found')
            response_body = b'File Not found'
            response = response_header + b'\r\n' + response_body
        else:               # 文件存在
            response_header = self.handle_headers('200', 'OK')
            response_body = f.read()
            response = response_header + b'\r\n' + response_body

        sock.send(response)
        # close socket
        sock.close()

    def handle_headers(self, status, phrease):
        '''10.处理handle_headers'''
        response_first_line = 'HTTP/1.1 %s %s\r\n' % (status, phrease)
        response_header = b'Server:MyWebServer\r\n'
        return response_first_line.encode(encoding='utf-8') + response_header


# 1.对HTTPServer的使用
def main():
    # 2.需要实例化HTTPServer这个类
    httpserver = HTTPServer()
    # 3.HTTPServer 应该具有绑定 (ip,port)的方法
    httpserver.bind()
    # 4.运行HTTPServer
    httpserver.start()


if __name__ == '__main__':
    main()
