#! /usr/bin/env python
# -*- coding:utf-8 -*-

# 定义一个类
class Calculator:
    # 类的属性
    name = "Smart calculator"
    price = 18.8

    # 初始化类
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # 类的方法
    def addition(self, x, y):
        result = x+y
        print("加法结果:", result)

    def subtraction(self, x, y):
        result = x-y
        print("减法结果:", result)

    def multiplication(self, x, y):
        result = x*y
        print("乘法结果:", result)

    def division(self, x, y):
        result = x/y
        print("除法结果:", result)


calculator = Calculator("小天才计算器", 99.99)
print(calculator)
print(calculator.name)
print(calculator.price)
print(calculator.addition(15, 3))
print(calculator.subtraction(15, 3))
print(calculator.multiplication(15, 3))
print(calculator.division(15, 3))
