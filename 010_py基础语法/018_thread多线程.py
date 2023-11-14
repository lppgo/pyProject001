#! /usr/bin/env python
# -*- coding:utf-8 -*-
import threading
import time

# 定义一个函数作为线程的执行体
def print_numbers():
    for i in range(1, 6):
        print(f"Number: {i}") # f 字符串用于在字符串中插入变量的值
        time.sleep(1)


def print_letters():
    for letter in 'abcde':
        print(f"Letter: {letter}")
        time.sleep(1)


# 创建两个线程
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# 启动线程
thread1.start()
thread2.start()

# 等待两个线程执行完成
thread1.join()
thread2.join()

print("Both threads have finished.")