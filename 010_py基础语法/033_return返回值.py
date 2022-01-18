#!/usr/bin/env python
# coding: utf-8


""
""" 
 global 和 return 
"""


""" 
 return 多返回值
 
"""

print("---------------- <1> 使用global (不推荐) --------------------")


def profile1():
    global name
    global age
    name = "Danny"
    age = 30


profile1()
print(name)
# Output: Danny
print(age)
# Output: 30


def profile2():
    name = "Danny"
    age = 30
    return (name, age)


print("---------------- <2> 返回tuple或者list --------------------")
profile_data = profile2()
print(profile_data[0])
# Output: Danny
print(profile_data[1])
# Output: 30


print("---------------- <3> 多返回值 --------------------")


def profile3():
    name = "Danny"
    age = 30
    return name, age


profile_data = profile3()
print(profile_data[0])
# Output: Danny
print(profile_data[1])
# Output: 30
