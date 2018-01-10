#!/usr/bin/env python
# coding=utf-8

"""
这是一个服务进程,服务进程负责启动Queue,把Queue注册到网络上,让后在Queue中
写入任务
"""
import random
import queue
from multiprocessing.managers import BaseManager


# 发送任务的队列:

task_queue = queue.Queue()

# 接受任务的队列

result_queue = queue.Queue()

"""
BaseManager: 将方法注册给BaseManager,当做方法一样调用
"""

# 从 BaseMananeger继承的QueueManager:


class QueueManager(BaseManager):
    pass


# 把两个Queue都注册到网络上,callable 参数关联了Queue对象

QueueManager.register('get_task_queue', callable=lambda: task_queue)

QueueManager.register('get_result_queue', callable=lambda: result_queue)

# __init__ 基本设置方法
# 绑定端口5000,设置密码为'abc', 空代表所有
manager = QueueManager(address=('', 5000), authkey=b'abc')

# 启动Queue 为此管理器对象生成一个服务器进程
manager.start()

# 获得通过网络访问的Queue对象
# 获得了2个队列对象
task = manager.get_task_queue()
result = manager.get_result_queue()

# 放几个任务进去
# 向 task 中put信息
for i in range(10):
    n = random.randint(0, 10000)
    print('Put task %d...' % n)
    task.put(n)

# 从result队列中读取结果
print('Try get results.....')
for i in range(10):
    r = result.get(timeout=10)
    print('result: %s' % r)

# 关闭

manager.shutdown()
print('master exit.')
