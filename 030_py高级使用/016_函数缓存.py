#!/usr/bin/env python
# coding: utf-8

from functools import lru_cache

"""
Python函数缓存是指通过使用缓存机制来存储已经计算过的函数调用结果，以避免重复计算，提高程序的运行效率。

函数缓存的实现通常通过使用装饰器来完成。Python标准库中提供了functools模块中的lru_cache装饰器，它可以用于函数缓存
"""

@lru_cache(maxsize=32)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


# 第一次调用时，函数的结果将会被缓存起来
print(fib(10))  # 输出: 55

# 第二次调用时，直接从缓存中获取结果，而不是再次计算
print(fib(10))  # 输出: 55

# print([fib(n) for n in range(100)])
# # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
