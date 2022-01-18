#! /usr/bin/env python
# -*- coding:utf-8 -*-

""
"""
-----------------------------列表list----------------------- 
List 列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套
List 是写在[]之间，用逗号分隔的元素列表

和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表

List 内置了有很多方法，例如 append()、pop() 等等，这在后面会讲到。

注意:
    1、List写在方括号[]之间，元素用逗号隔开。
    2、和字符串一样，list可以被索引和切片。
    3、List可以使用+操作符进行拼接。
    4、List中的元素是可以改变的。

 """
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
for i, v in enumerate(["tic", "tac", "toe"]):
    print(i, v)

# 同时遍历两个或更多的序列，可以使用 zip() 组合:
questions = ["name", "quest", "favorite color"]
answers = ["lancelot", "the holy grail", "blue"]
for q, a in zip(questions, answers):
    print("What is your {0}?  It is {1}.".format(q, a))

# 要反向遍历一个序列，首先指定这个序列，然后调用 reversed() 函数
# for i in range(1, 10, 2):
#     print(i)
for i in reversed(range(1, 10, 2)):
    print(i)
