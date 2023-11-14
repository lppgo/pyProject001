#!/usr/bin/env python
# coding: utf-8

from functools import wraps
"""
类装饰器是 Python 中一种高级的装饰器形式，它允许你使用类来装饰函数或方法。
类装饰器通常需要实现 __init__ 和 __call__ 方法，其中 __init__ 在装饰器实例化时调用，而 __call__ 在实际装饰过程中调用
"""

class MyDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Decorating the function")
        result = self.func(*args, **kwargs)
        print("Function decorated")
        return result

@MyDecorator
def my_function():
    print("Inside the function")

# 调用装饰后的函数
my_function()
