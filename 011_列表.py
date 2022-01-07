#! /usr/bin/env python
# -*- coding:utf-8 -*-

# -----------------------------列表list-----------------------

# list 使用[]
# list 中的元素类型可以不一样
# list 中的元素可以被修改
#
#

# 定义列表List
a_list = [1, 3, 3, 3, 8, 5, "verbose"]
print(a_list)
# list操作
a_list.append(7)
a_list.insert(0, 2)
# 删除第一个value=3的元素
a_list.remove(3)
print("a_list:", a_list)
# 获取最后一个元素，负索引开始
print("a_list的最后一个元素是:", a_list[-1])
# 获取元素的索引index
print("1在a_list中的索引:", a_list.index(1))
# 获取元素在list出现的次数
print("3在a_list出现的次数:", a_list.count(3))

# 排序
# a_list.sort()
# print("正排序 a_list:", a_list)
# a_list.sort(reverse=True)
# print("逆排序 a_list:", a_list)

for index in range(len(a_list)):
    print("index=", index, "elements in a_lit=", a_list[index])

# -----------------------------多维列表list-----------------------
# 库 numpy pandas
multi_list = [
    [1, 2, 3, 4, 5],
    [10, 20, 30, 40, 50],
    [11, 12, 13, 14, 15],
]

print(multi_list[0])  # 打印第1维
print(multi_list[1][2])  # 打印第2维索引是2的元素

# ----------------------------- 遍历 --------------------------
# 在序列中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到:
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# 同时遍历两个或更多的序列，可以使用 zip() 组合:
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

# 要反向遍历一个序列，首先指定这个序列，然后调用 reversed() 函数
# for i in range(1, 10, 2):
#     print(i)
for i in reversed(range(1, 10, 2)):
    print(i)
