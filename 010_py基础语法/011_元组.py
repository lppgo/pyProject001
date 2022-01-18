#! /usr/bin/env python
# -*- coding:utf-8 -*-

""
"""
 -----------------------------元组tuple-----------------------
tuple 使用小括号()
tuple 中的元素类型可以不一样
tuple 中的元素不可以被修改
tuple 可以使用下标索引来访问元组中的值
tuple 中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组
tuple + * 可以对元组进行组合和复制

"""

# 定义元组tuple
a_tuple = (1, 2, 3, 4, 5, "lucas")
for x in a_tuple:
    print(x)

b_tuple = 10, 12, 214, 1245
for index in range(len(b_tuple)):
    print("index=", index, "elements in b_tuple", b_tuple[index])
