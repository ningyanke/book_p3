#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
tftp上传
"""
from socket import *
import struct


def main():
    myfile = open('线程udp服务端.py', 'rb')     # 打开文件
    udpsocket = socket(AF_INET, SOCK_DGRAM)    # 创建socket
    destaddr = ('10.115.28.13', 69)
    data = struct.pack('!H8sb5sb', 2, b'test1.py', 0, b'octet', 0)
    udpsocket.sendto(data, destaddr)   # 发送写入的报文

    blocknum = 0
    while True:
        recvdata, recvaddr = udpsocket.recvfrom(1024)  # 接受报文,返回要写入的文件序号
        recvnum = struct.unpack('!H', recvdata[2:4])[0]
        print(recvnum)
        data1 = myfile.read(512)
        if blocknum == recvnum:
            blocknum += 1
            if blocknum == 65536:
                blocknum = 0
            blockdata1 = struct.pack(
                '!HH{}s'.format(len(data1)), 3, blocknum, data1)
            print(blocknum)
            udpsocket.sendto(blockdata1, recvaddr)
            if len(data1) < 512:
                break


if __name__ == '__main__':
    main()
