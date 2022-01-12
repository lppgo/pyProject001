#!/usr/bin/env python

import threading
import time


class myThread(threading.Thread):
    def __init__(self, threadID, name, delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = delay

    def run(self):
        print("开始线程 :{}".format(self.name))
        # 获取锁，用于线程同步
        threading.Lock.acquire()
        print_time(self.name, self.delay, 3)
        # 释放锁
        print("退出线程 :{}".format(self.name))
        threading.Lock.release()


def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1


threads = []

# 创建新线程
thread1 = myThread(1, "thread-1", 2)
thread2 = myThread(2, "thread-2", 2)
thread3 = myThread(3, "thread-3", 3)

# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)
threads.append(thread3)

print(time.ctime(time.time()))
# 开启新线程
for t in threads:
    t.start()

# 等待所有线程完成
for t in threads:
    t.join()
print("子线程完成 ...")

print("退出主线程 ... ")
