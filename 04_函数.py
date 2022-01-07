#! /usr/bin/env python
# -*- coding:utf-8 -*-


# def myfunc():
#     print("this is a function !")
#     a = 1
#     b = 100
#     print(a + b)
#
#
# def say(name):
#     print("hi : " + name)
#
#
# myfunc()
# say("lucas")


def sale(price, time, colour="red", brand="奥迪"):
    print("price:", price,
          "colour:", colour,
          "brand:", brand,
          "time:", time)

    return "this car is saled!"


print(sale(10000, "2020-10", brand="奔驰"))


""" --------------- lambda 匿名函数 ----------------------- """
def sum(arg1, arg2): return arg1 + arg2


print("相加后的值为 : ", sum(10, 20))
print("相加后的值为 : ", sum(20, 20))
