#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time


'''
现在只需要一个入口,对客户端隐藏细节:
    需要设计一个Application类,专门处理所有的入口文件,不管是 .py 动态 还是 html 静态
    需要引入 HTTPServer 类,将Application() 加载去处理 WSGI 规定的框架结构
    需要一个 路由映射文件来处理 文件名和 函数的对应
'''

HTML_ROOT_DIR = './html_page'


class AppliCation:
    '''1.处理所有动态,静态入口'''

    def __init__(self, urls):
        self.urls = urls

    def __call__(self, env, handle_headers):
        filename = env.get('PATH')

        # 约定客户端使用 /static/xxx.html 访问的全部都是静态的页面
        if filename.startswith('/static'):
            if '/' == filename:
                filename = '/index.html'
            try:
                with open(HTML_ROOT_DIR + filename[7:], 'rb') as f:
                    msg = f.read()
            except IOError as e:   # 文件不存在
                status = '404 Not Found'
                headers = []
                handle_headers(status, headers)
                return b'File Not Found'
            else:               # 文件存在
                status = '200 OK'
                headers = [
                    ('Content-Type', 'text/html')
                ]
                handle_headers(status, headers)

                return msg

        # 判断filename时候存在 urls 中,如果存在,调用对应的方法,不存在,返回 404
        for file, app in self.urls:
            if file == filename:
                return app(env, handle_headers)

        status = '404 Not Found'
        headers = []
        handle_headers(status, headers)
        return b'File Not Found'


# def application(env, handle_headers):
def mytime(env, handle_headers):
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain')
    ]
    handle_headers(status, headers)
    return time.ctime()


def sayhi(env, handle_headers):
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain')
    ]
    handle_headers(status, headers)
    return b'hi'


urls = [
    ('/mytime', mytime),
    ('/sayhi', sayhi)
]

app = AppliCation(urls)

# def main():
#     # 10.urls 路由映射
#     urls = [
#         ('/mytime', mytime),
#         ('/sayhi', sayhi)
#     ]
#     # 11.传入AppliCation
#     # 2.实例化
#     app = AppliCation(urls)
#     # 3.让HTTPServer加载app去处理 WSGI
#     httpserver = HTTPServer(app)
#     # 5.改写HTTPServer
#     # 6.绑定
#     httpserver.bind()
#     # 7.启动
#     httpserver.start()


# if __name__ == '__main__':
#     main()
