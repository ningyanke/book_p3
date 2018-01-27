#!/usr/bin/env python
# coding=utf-8
# author:ning

from socket import *
import struct


def main():
    myfile = open('123.pdf', 'ab')
    udpsocket = socket(AF_INET, SOCK_DGRAM)
    destaddr = ('10.115.28.13', 69)
    data = struct.pack('!H7sb5sb', 1, b'123.pdf', 0, b'octet', 0)
    udpsocket.sendto(data, destaddr)
    num = 0
    while True:
        recvdata, recvaddr = udpsocket.recvfrom(1024)
        opernum = struct.unpack('!H', recvdata[:2])[0]
        if opernum == 3:
            myfile.write(recvdata[4:])
            blocknum = struct.unpack('!H', recvdata[2:4])[0]
            print(blocknum)

            num += 1
            if num == 65536:
                num = 0

            if num == blocknum:
                num = blocknum
                ack = struct.pack('!HH', 4, blocknum)
                udpsocket.sendto(ack, recvaddr)
                if len(recvdata) < 516:
                    myfile.close()
                    break
        elif opernum == 5:
            myfile.close()
            break


if __name__ == '__main__':
    main()
