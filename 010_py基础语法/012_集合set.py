#! /usr/bin/env python
# -*- coding:utf-8 -*-

""
"""
---------------set 集合----------------------

集合（set）是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员。
集合内的元素无序且不重复;

基本功能是进行成员关系测试和删除重复元素。

可以使用大括号 { } 或者 set() 函数创建集合，
注意:创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。

 """

# 创建一个集合
mySet = {"C", "C++", "Ruby", "PHP", "JAVA", "Python", "Go", "Rust", "C++"}
print(mySet)  # 输出集合，重复的元素被自动去掉

# 成员测试
if "Go" in mySet:
    print("Go 在集合中")
else:
    print("Go 不在集合中")

# set可以进行集合运算
a = set("abcdefghijklmn")
b = set("aefgxyz")

print("a和b的差集: ", a - b)
print("a和b的并集: ", a | b)
print("a和b的交集: ", a & b)
print("a和b的不同时存在的元素(并集-交集): ", a ^ b)  # 并集减交集
