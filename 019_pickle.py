#! /usr/bin/env python
# -*- coding:utf-8 -*-

import pickle

""" --------------------- pickle模块 实现了基本的数据序列和反序列化 ------------------------- """
# 通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储
# 通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象

a_dict = {"da": 111, 2: [11, 2, 3], "three": {1: 10, "e": "lambda"}}

# dump

# file = open("dump.pickle", "wb")
# pickle.dump(a_dict, file)
# file.close()

# load
# file = open("dump.pickle", "rb")
# b_dict = pickle.load(file)
# file.close()
# print(a_dict == b_dict)  # True

# # 使用with open file,有自动close
with open("dump.pickle", "rb") as file:
    c_dict = pickle.load(file)
print(a_dict == c_dict)  # True
