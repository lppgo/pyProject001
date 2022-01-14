#!/usr/bin/env python
# coding: utf-8
from enum import Enum, unique

Month = Enum(
    "Month",
    (
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
    ),
)
# 可以直接使用Month.Jan来引用一个常量：
print(Month.Jan.value)
# 枚举所有成员：
for name, member in Month.__members__.items():
    print(name, "=>", member, ",", member.value)


# value属性则是自动赋给成员的int常量，默认从1开始计数

# 如果想自定义value值 :
# @unique装饰器可以帮助我们检查保证没有重复值。如果重复了，会报ValueError错误
@unique
class Month(Enum):
    Jan = 0
    Feb = 1
    Mar = 2


print(Month.Jan.value)
for name, member in Month.__members__.items():
    print(name, "=>", member, ",", member.value)
