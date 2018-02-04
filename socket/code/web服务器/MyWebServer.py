#!/usr/bin/env python
# -*- coding: utf-8 -*-


from socket import *
from multiprocessing import Process
import re
import sys

HTML_ROOT_DIR = './html_page'


class HTTPServer:
    '''将web服务器看做一个整体,它应该具有自己的方法和属性'''

    def __init__(self, application):
        self.sersocket = socket(AF_INET, SOCK_STREAM)
        self.app = application

    def bind(self, ip='', port=8899):
        self.sersocket.bind((ip, port))
        self.sersocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    def start(self, num=5):
        self.sersocket.listen(num)
        while True:
            newsocket, cliaddr = self.sersocket.accept()
            p1 = Process(target=self.handle_cli, args=((newsocket,)))
            p1.start()

    def handle_cli(self, sock):
        recvmsg = sock.recv(1024).decode(encoding='utf-8')
        request_first_line = recvmsg.split('\r\n')[0]
        # user re get filename
        patt = '\w+ (/[^ ]*)'
        filename = re.match(patt, request_first_line).group(1)
        option = re.match('(\w+) /[^ ]*', request_first_line).group(1)

        # create env
        env = {
            'PATH': filename,
            'OPTION': option
        }

        # handle_headers 处理response返回的数据的头部
        # 对解析到的request 的首部文件是 .py结尾的文件进行判断
        # if filename.endswith('.py'):   # .py文件
        #     try:
        #         m = __import__(filename[1:-3])   # 动态导入
        #     except Exception as e:
        #         response_header = self.handle_headers('404', 'Not Found')
        #         response_body = b'File Not found'
        #         response = response_header + b'\r\n' + response_body
        #     else:
        #         response_body = m.application(env, self.handle_headers)
        #         response = bytes(self.response_header, 'utf-8') + b'\r\n' + \
        #             response_body.encode(encoding='utf-8')
        # else:
        #     if '/' == filename:
        #         filename = '/index.html'
        #     try:
        #         f = open(HTML_ROOT_DIR + filename, 'rb')
        #     except IOError as e:   # 文件不存在
        #         response_header = self.handle_headers('404', 'Not Found')
        #         response_body = b'File Not found'
        #         response = response_header + b'\r\n' + response_body
        #     else:               # 文件存在
        #         response_header = self.handle_headers('200', 'OK')
        #         response_body = f.read()
        #         response = response_header + b'\r\n' + response_body

        response_body = self.app(env, self.handle_headers)
        if isinstance(response_body, bytes):
            response = bytes(self.response_header, 'utf-8') + \
                b'\r\n' + response_body
        else:
            response = bytes(self.response_header, 'utf-8') + b'\r\n' + \
                response_body.encode(encoding='utf-8')

        sock.send(response)
        # close socket
        sock.close()

    def handle_headers(self, status, headers):
        response_first_line = 'HTTP/1.1 ' + status + '\r\n'
        response_header = ''
        for header in headers:
            response_header += '%s:%s\r\n' % header
        self.response_header = response_first_line + response_header


# 1.对HTTPServer的使用

def main():
    # 导入模块文件
    Python_Model_dir = './dynamic'
    sys.path.insert(1, Python_Model_dir)
    # 2.需要实例化HTTPServer这个类
    httpserver = HTTPServer()
    # 3.HTTPServer 应该具有绑定 (ip,port)的方法
    httpserver.bind()
    # 4.运行HTTPServer
    httpserver.start()


if __name__ == '__main__':
    main()
