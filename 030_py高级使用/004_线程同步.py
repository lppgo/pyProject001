#!/usr/bin/env python

import threading


lock = threading.Lock()
amount = 0


def changeValue(x):
    global amount
    amount = amount + x
    amount = amount - x


# 批量运行改值
def batchRunThread(x):
    for i in range(100000):
        lock.acquire()  # 获取锁
        try:
            changeValue(x)
        finally:
            lock.release()  # 释放锁


# 创建2个线程
t1 = threading.Thread(target=batchRunThread, args=(5,), name="Thread1")
t2 = threading.Thread(target=batchRunThread, args=(15,), name="Thread2")
t1.start()
t2.start()
t1.join()
t2.join()
print("子线程完成 ...")

print(amount)

print("退出主线程 ... ")


"""
多线程与多进程最大的不同就是：对于同一个变量，对于多个线程是共享的，但多进程里每个进程各自会copy一份;
所以，多线程一个重要的问题是多线程之间同步，方式数据竞态；
线程的调度是由OS决定的
"""
