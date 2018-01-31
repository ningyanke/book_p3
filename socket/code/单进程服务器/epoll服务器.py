#!/usr/bin/env python
# -*- coding: utf-8 -*-


from socket import *
import select


def main():
    # create socket
    sersocket = socket(AF_INET, SOCK_STREAM)
    # bind
    ipaddr = ('', 8899)
    sersocket.bind(ipaddr)
    # listen
    sersocket.listen(5)

    # create epoll
    epoll = select.epoll()

    # 测试文件描述符
    # print(sersocket.fileno())
    # $ python epoll服务器.py
    # 3

    '''
    注册事件到epoll中
    epoll.register(fd[, eventmask])
    如果fd已经注册过,则会抛出异常
    '''
    # 将创建好的套接字加入epoll
    # EPOLLIN 接受数据
    # EPOLLOUT 发送数据
    # EPOLLET ET模式,
    # epoll对文件描述符操作有2中模式:LT(默认),ET,
    # LT 当epoll检测到数据描述符事件发生通知程序,程序可以不立即执行,下次调用epoll,会再次相应执行
    # ET 当epoll检测到数据描述符事件发生通知程序,程序必须立即执行,否则,下次不会在执行
    epoll.register(sersocket.fileno(), select.EPOLLIN | select.EPOLLET)

    # 创建字典保存客户端连接的对象
    connections = {}
    addrsses = {}

    # accept
    while True:
        # epoll 接受文件描述符改变后 内核返回的事件,如果不设置超时,默认阻塞等待
        epoll_list = epoll.poll()

        # 对事件进行判断
        for fd, events in epoll_list:
            # print(fd)
            # print(events)
            # 3
            # 1

            # 如果是sersocket,代表有新的客户端连接
            if fd == sersocket.fileno():
                newsocket, cliaddr = sersocket.accept()
                print('来自{}的连接'.format(cliaddr))
                # 创建字典保存客户端的连接对象
                connections[newsocket.fileno()] = newsocket
                addrsses[newsocket.fileno()] = cliaddr

                # 想epoll中注册连接socket的事件
                epoll.register(newsocket.fileno(),
                               select.EPOLLIN | select.EPOLLET)

            elif events == select.EPOLLIN:
                # 接受数据
                msg = connections[fd].recv(1024)
                if msg:
                    print('{}:{}'.format(
                        addrsses[fd], msg.decode(encoding='utf-8')))
                else:
                    print('{} 断开了连接'.format(addrsses[fd]))
                    # 客户段调用了close()
                    # 取消注册的socket
                    epoll.unregister(fd)
                    connections[fd].close()
                    del connections[fd]
                    del addrsses[fd]


if __name__ == '__main__':
    main()
