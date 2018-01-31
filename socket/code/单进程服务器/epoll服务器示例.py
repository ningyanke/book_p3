import socket
import select  #: epoll包含在select模块中

EOL1 = b'\n\n'
EOL2 = b'\n\r\n'
response = b'HTTP/1.0 200 OK\r\nDate: Mon, 1 Jan 1996 01:01:01 GMT\r\n'
response += b'Content-Type: text/plain\r\nContent-Length: 13\r\n\r\n'
response += b'Hello, world!'

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.bind(('0.0.0.0', 8080))
serversocket.listen(1)
serversocket.setblocking(0)  #: 默认情况下，socket处于阻塞模式

epoll = select.epoll()       #: 创建一个epoll对象
# 在serversocket上注册读事件，读事件发生在serversocket每次接受socket连接时
epoll.register(serversocket.fileno(), select.EPOLLIN)

try:
    # 文件描述符（整数）与其对应的网络连接对象的映射
    connections = {}
    requests = {}
    responses = {}
    while True:
        # 查询epoll对象，看是否有感兴趣的事件发生
        # 参数`1`表明我们最多会等待1秒钟
        # 如果在这次查询之前有我们感兴趣的事件发生，这次查询将会立即返回这些事件的列表
        events = epoll.poll(1)
        # 事件是一个`(fileno, 事件code)`的元组
        for fileno, event in events:
            # 如果serversocket上发生了读事件，那么意味着有一个有新的连接
            if fileno == serversocket.fileno():
                connection, address = serversocket.accept()
                # 将新的socket设为非阻塞
                connection.setblocking(0)
                # 给新创建的socket注册读事件（EPOLLIN），表明将有数据请求
                epoll.register(connection.fileno(), select.EPOLLIN)
                connections[connection.fileno()] = connection
                # 收集各客户端来的请求
                requests[connection.fileno()] = b''
                responses[connection.fileno()] = response
            elif event & select.EPOLLIN:
                # 如果发生了读事件，从客户端读取数据
                requests[fileno] += connections[fileno].recv(1024)
                if EOL1 in requests[fileno] or EOL2 in requests[fileno]:
                    # 一旦请求被完全接收了，注销这个socket的读事件，然后注册写事件（EPOLLOUT）
                    # 表明响应即将开始
                    # 当向客户端发送响应的时候，读事件发生
                    epoll.modify(fileno, select.EPOLLOUT)
                    # 打印出完整的请求
                    # 结果表明：尽管客户端请求交错发生，每一个客户端的请求仍然能被聚合起来
                    print('-' * 40 + '\n' + requests[fileno].decode()[:-2])
            elif event & select.EPOLLOUT:
                # 如果发生了写事件，向客户端发送响应
                # 每次向客户端发送一定长度的响应内容，每次都更新余下待发送的响应内容
                byteswritten = connections[fileno].send(responses[fileno])
                responses[fileno] = responses[fileno][byteswritten:]
                # 响应已经发送完毕，一次请求/响应周期完成，不再监听该socket的事件了
                if len(responses[fileno]) == 0:
                    epoll.modify(fileno, 0)
                # 告诉客户端，关闭连接
                connections[fileno].shutdown(socket.SHUT_RDWR)
            # `HUP`（挂起）事件表明客户端断开了连接
            elif event & select.EPOLLHUP:
                # 注销对断开客户端socket的事件监听
                epoll.unregister(fileno)
                # 关闭连接，服务端关闭
                connections[fileno].close()
                del connections[fileno]
finally:
    epoll.unregister(serversocket.fileno())
    epoll.close()
    serversocket.close()
