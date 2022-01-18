#!/usr/bin/env python
# coding: utf-8

from functools import reduce


""""""
""" 
  ------------- filter() 过滤函数 ------------------
filter()  filter过滤列表中的元素，并且返回一个由所有符合要求的元素所构成的列表，符合要求即函数映射到该元素时返回值为True
"""


def f1(x):
    return x > 50


""" 
  ------------- map() 映射函数 ------------------
map() 会将一个函数映射到一个输入列表的所有元素上
"""


def f2(x):
    return x * 2


raw_data = [10, 20, 30, 40, 50, 60, 70, 80]

filtered_data = filter(f1, raw_data)
f1_res_data = list(filtered_data)
print(raw_data)
print(f1_res_data)

filtered_data = map(f2, raw_data)
f2_res_data = list(filtered_data)
print(raw_data)
print(f2_res_data)

""" 
  ------------- reduce() 函数 ------------------
reduce() 当需要对一个列表进行一些计算并返回结果时，适用于reduce()
"""

product = reduce((lambda x, y: x * y), [1, 2, 3, 4, 5])
print("reduce()函数对一个list 进行乘积，结果是product={}".format(product))
