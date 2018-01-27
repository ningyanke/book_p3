#!/usr/bin/env python
# coding=utf-8


"""
实现tftp下载功能
根据tftp的报文流程构造数据包
"""

from socket import *
import struct


# 使用的是UDP协议
clisocket = socket(AF_INET, SOCK_DGRAM)


# 发送下载请求
ip = '10.115.28.13'
port = 69
ip_port = (ip, port)
filename = b'test.py'
len_filename = len(filename)
msg = struct.pack('!H{}sb5sb'.format(len_filename),
                  1, filename, 0, b'octet', 0)
clisocket.sendto(msg, ip_port)

# 服务器回应消息
recvmsg = clisocket.recvfrom(1024)
recvmsg1, recvmsg2 = recvmsg
print(recvmsg1.decode(encoding='utf-8'), recvmsg2)
'''
recvmsg1 头部包含了 操作码和块编号
recvmsg2: 返回一个元组,包括服务器地址和返回的端口号
('10.115.28.13', 52758)
'''

# 发送确认报文
num = struct.unpack('!HH', recvmsg1[:4])
print(num)
ackmsg = struct.pack('!HH', 4, num[1])
clisocket.sendto(ackmsg, ip_port)
