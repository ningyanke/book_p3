#!/usr/bin/evn python
# coding=utf-8

import time
import multiprocessing

def fun(val):
    for i in range(10):
        time.sleep(0.5)
        with val.get_lock():
            val.value += 1

v = multiprocessing.Value('i', 0)
p_list = [multiprocessing.Process(target=fun, args=(v, )) for i in range(10)]
for p in p_list:
    p.start()

for p in p_list:
    p.join()

print(v.value)
