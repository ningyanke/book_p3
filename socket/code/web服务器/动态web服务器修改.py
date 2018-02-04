#!/usr/bin/env python
# -*- coding: utf-8 -*-


from socket import *
from multiprocessing import Process
import re
import sys

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
        option = re.match('(\w+) /[^ ]*', request_first_line).group(1)

        # create env
        env = {
            'PATH': filename,
            'OPTION': option
        }

        # handle_headers 处理response返回的数据的头部
        # set index html page

        # 对解析到的request 的首部文件是 .py结尾的文件进行判断
        # /mytime.py
        if filename.endswith('.py'):   # .py文件
            try:
                m = __import__(filename[1:-3])   # 动态导入
                # 测试点
                print(1)
                print(filename[1:-3])
            except Exception as e:
                # 测试点
                print(2)
                response_header = self.handle_headers('404', 'Not Found')
                response_body = b'File Not found'
                response = response_header + b'\r\n' + response_body
            else:
                """
                WSGI接口定义,要求Web开发者实现一个函数, 可以响应HTTP请求
                def application(environ, start_response):
                    start_response('200 OK', [('Content-Type', 'text/html')])
                    return 'Hello World!
                上面的application()函数就是符合WSGI标准的一个HTTP处理函数，它接收两个参数：

                environ：一个包含所有HTTP请求信息的dict对象；
                start_response：一个发送HTTP响应的函数。
                整个application()函数本身没有涉及到任何解析HTTP的部分，也就是说，把底层web服务器解析部分
                和应用程序逻辑部分进行了分离，这样开发者就可以专心做一个领域了不过，等等，这个application()
                函数怎么调用？如果我们自己调用，两个参数environ和start_response我们没法提供，返回的str也没法发给浏览器。

                所以application()函数必须由WSGI服务器来调用。有很多符合WSGI规范的服务器。而我们此时的web服务器的目的
                就是做一个极可能解析静态网页还可以解析动态网页的服务器
                """
                # 测试点
                print(dir(m))
                response_body = m.application(env, self.handle_headers)

                # response_header = self.handle_headers('200', 'OK')
                # response_body = m.application()
                # 测试点
                print(response_body)
                response = bytes(self.response_header, 'utf-8') + b'\r\n' + \
                    response_body.encode(encoding='utf-8')
        else:
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

    def handle_headers(self, status, headers):
        '''
        10.处理handle_headers
            status = '200 OK'
        headers = [
            ('Content-Type', 'text/plain')
        ]
        '''

        """
        response_first_line = 'HTTP/1.1 %s %s\r\n' % (status, phrease)
        response_header = b'Server:MyWebServer\r\n'
        return response_first_line.encode(encoding='utf-8') + response_header
        """
        response_first_line = 'HTTP/1.1 ' + status + '\r\n'
        response_header = ''
        for header in headers:
            response_header += '%s:%s\r\n' % header
        # 测试点
        print(response_header)
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
