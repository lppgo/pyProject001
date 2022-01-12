#! /usr/bin/env python
# -*- coding:utf-8 -*-
import copy


a = [1, 2, 3]
b = a  # 相同的内存引用
# id  查看内存索引
print(id(a))
print(id(b))
print(id(a) == id(b))  # True
# -------------------copy------------------------
c = copy.copy(a)
print(id(a) == id(c))  # False

a = [1, 2, [3, 4]]
d = copy.copy(a)
print(id(a) == id(d))  # False
print(id(a[2]) == id(c[2]))  # ???

# -------------------deeepcopy------------------------
# copy.deepcopy()
