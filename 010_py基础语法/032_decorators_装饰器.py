#!/usr/bin/env python
# coding: utf-8


""
"""
---------------- Decorators 装饰器 --------------------
- 是修改其他函数的功能的函数;
- 函数也可以是对象;
- 在函数中定义函数;
- 在函数中返回函数;
- 将函数作为参数传给另一个函数;



"""

print("------------------------ <1> -------------------------------")


def a_new_decorator(fn):
    def wrapThefn():
        print("the fn execution before ...")
        fn()
        print("the fn execution after ...")

    return wrapThefn()


def greet():
    print("fn do something ! ")


wrap_greet = a_new_decorator(greet)
wrap_greet

print("------------------------ <2> -------------------------------")

""" 使用@来装饰 
the @a_new_decorator is just a short way of saying:
    hello=a_new_decorator(hello)
"""


@a_new_decorator
def hello():
    print("hello ! ")


hello

print("------------------------ <3> -------------------------------")


from functools import wraps


def decorator_name(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not can_run:
            return "Function will not run"
        return f(*args, **kwargs)

    return decorated


@decorator_name
def func():
    return "Function is running"


can_run = True
print(func())
# Output: Function is running
can_run = False
print(func())
# Output: Function will not run
