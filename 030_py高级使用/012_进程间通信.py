#!/usr/bin/env python
# coding: utf-8


import multiprocessing as mp
import os
import time

"""
   --------------- 进程间通信 -------------
multiprocessing 支持进程之间的两种通信通道:
    1 : Queue 队列，Queue 类是一个近似 queue.Queue 的克隆;
    2 : Pipe() 管道，Pipe()函数返回一个由管道连接的连接的连接对象，默认是双向的;

"""


def write(q):
    print("write Process %s is running ..." % (os.getpid()))
    for x in ["Python", "Java", "C++", "Go", "Rust"]:
        q.put(x)
        print("write to Queue : %s " % (x))


def read(q):
    print("read Process %s is running ..." % (os.getpid()))
    while True:
        item = q.get(True)
        print("read from Queue :%s " % (item))


if __name__ == "__main__":
    print("Main Process %s is running ... " % (os.getpid()))
    q = mp.Queue(3)

    p1 = mp.Process(target=write, args=(q,))
    p2 = mp.Process(target=read, args=(q,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
