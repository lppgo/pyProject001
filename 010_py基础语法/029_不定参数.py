#!/usr/bin/env python
# coding: utf-8

""""""
""" 
  ------------- 不定参数 ------------------
1 : *args : 发送一个非键值对的可变数量的参数列表给一个函数

2 : **kwargs : 允许你将不定长度的键值对, 作为参数传递给一个函数

"""


def test_var_args(f_arg, *argv):
    print("first normal arg:%s" % (f_arg))
    for x in argv:
        print("another arg through *argv:{}".format(x))


test_var_args("yasoob", "python", "eggs", "test")


def test_var_kwargs(**kwargv):
    for key, value in kwargv.items():
        print("{0} : {1}".format(key, value))


test_var_kwargs(name="lucas", age=28, industry="IT")


""" 
  ------------- 使用*args **kwargs  来传参 ------------------
"""
args = ("two", 2, 3, 3.14)
test_var_args(*args)

kwargs = {"name": "lucas", "age": 28, "subject": "it"}
test_var_kwargs(**kwargs)
