#!/usr/bin/env python
# coding=utf-8

"""
使用数组的方式共享内存和全局对象
Value: 返回一个从共享内存中分配的对象
    Value.value : 得到Value中Ctype的值
    Value.get_lock: 获取 Value中的锁对象
    Vlaue.acquie/release 上锁/释放锁
Array: 返回一个从共享内存中分配的数组
"""

import os
from multiprocessing import Process, Array, Value

procs = 3
count = 0


def showdate(label, val, arr):
    """
    在这个进程中打印数据值
    """
    msg = '%-12s:pid:%4s, global:%s,value:%s,array:%s'
    print(msg % (label, os.getpid(), count, val.value, list(arr)))


def updater(val, arr):
    """通过共享内存进行通信"""
    global count
    count += 1  # 全局的基数器,非共享的
    # 传入的数据Value,Array是共享的
    val.value += 1
    for i in range(3):
        arr[i] += 1

if __name__ == '__main__':
    """
    Value, Array 返回的是一个内存中共享的Ctype对象
    i --> sigint --> int
    d ---> float,
    porcs 整数,确定了数组的长度,并且被初始化为 0

    因为这里是浮点类型,被初始化为0.0
    """
    scalar = Value('i', 0)
    vector = Array('d', procs)

    # 在父进程中显示起始值
    showdate('parent start', scalar, vector)

    # 派生子进程, 传入共享内存
    p = Process(target=showdate, args=('child', scalar, vector))
    p.start()
    p.join()

    # 传入父进程中跟新过的共享内存,等待每次传入结束
    # 每个子进程看到了父进程中到现在为止对args的跟新(但是全局变量看不到)
    print('\nloop1(updates in parent, serial children)....')
    for i in range(procs):
        count += 1
        scalar.value += 1
        vector[i] += 1  # 数组中的每个元素加1
        p = Process(target=showdate, args=(
            ('porcess %s ' % i), scalar, vector))
        p.start()
        p.join()

    # 同上,不过允许子进程单行运行
    # 所有进程都看到了最近一次的迭代结果,因为他们都共享这个对象
    print('\nloop2(updates in parent, serial children)....')
    ps = []
    for i in range(procs):
        count += 1
        scalar.value += 1
        vector[i] += 1
        p = Process(target=showdate, args=(
            ('porcess %s ' % i), scalar, vector))
        p.start()
        ps.append(p)
    for p in ps:
        p.join()

    # 共享内存在派生子进程中进行跟新,等待每个跟新结束
    print('\nloop3(updates in parent, serial children)....')
    for i in range(procs):
        p = Process(target=updater, args=(scalar, vector))
        p.start()
        p.join()

    showdate('parent temp', scalar, vector)

    # 同上, 不过允许子进程并行的进行更新
    ps = []
    print('\nloop4(updates in parent, serial children)....')
    for i in range(procs):
        p = Process(target=updater, args=(scalar, vector))
        p.start()
        ps.append(p)
    for p in ps:
        p.join()
    # 仅在父进程中全局变量count = 6

    # 在此显示最终的结果
    showdate('parent end', scalar, vector)
