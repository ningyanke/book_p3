"""
udp聊天服务端
"""
from socket import *


def main():
    sersocket = socket(AF_INET, SOCK_DGRAM)
    ip = ""    # 指定所有的网卡都可以用来接收消息
    port = 8899
    ip_port = (ip, port)
    bufsize = 1024
    sersocket.bind(ip_port)
    while True:
        msg = sersocket.recvfrom(bufsize)
        msg1, msg2 = msg
        print("\r>>>", msg1.decode(encoding='utf-8'))
        data = input("\r<<<")
        sersocket.sendto(data.encode(encoding='utf-8'), msg2)


if __name__ == '__main__':
    main()