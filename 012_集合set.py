#! /usr/bin/env python
# -*- coding:utf-8 -*-


# ---------------set 集合----------------------
# 集合（set）是一个无序的不重复元素序列
# 可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典


basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana', 10}

print(basket)  # 去重功能

print('orange' in basket)  # 快速判断元素是否在set内
