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


def main():
    # 导入模块文件
    Python_Model_dir = './dynamic'
    sys.path.insert(1, Python_Model_dir)
    '''
    想要使用的形式:
        python MyWebServer MyFrame:app
    可以使用sys.argv 来截取后面的参数
    '''
    modle_name, entry_obj = sys.argv[1].split(':')
    m = __import__(modle_name)
    # 从模块这个整体中导入实体对象,实体对象是模块的属性
    app = getattr(m, entry_obj)
    httpserver = HTTPServer(app)
    httpserver.bind()
    httpserver.start()


if __name__ == '__main__':
    main()
