#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

"""
1.第一版
def application():
    return time.ctime()
"""


def application(env, handle_headers):
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain')
    ]
    handle_headers(status, headers)
    return time.ctime()


if __name__ == '__main__':
    env = {}

    def handle_headers(status, headers):
        return 'HH'
    m = application(env, handle_headers)
    print(m)
