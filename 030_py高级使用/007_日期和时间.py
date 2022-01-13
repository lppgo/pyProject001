#!/usr/bin/env python


""""""
"""
Python 提供了一个 time 和 calendar 模块可以用于格式化日期和时间

时间间隔是以秒为单位的浮点小数 ;

每个时间戳都以自从 1970 年 1 月 1 日午夜（历元）经过了多长时间来表示 ;
"""

import time
import calendar

# 获取当前时间
print(time.time())
print(time.localtime())
# 获取格式化的时间
localtime1 = time.localtime(time.time())
print("repr       : {}".format(repr(localtime1)))
print("localtime1 : {}".format(localtime1))


localtime2 = time.asctime(time.localtime(time.time()))
print("localtime2 : {}".format(localtime2))


# 格式化时间
# 格式化成2016-03-20 11:45:39形式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# 格式化成Sat Mar 28 22:24:24 2016形式
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

# 将格式化时间字符串转为时间戳
ts1 = "2022-01-12 11:21:18"
print("ts1 : {}".format(time.mktime(time.strptime(ts1, "%Y-%m-%d %H:%M:%S"))))
ts2 = "Wed Jan 12 11:21:18 2022"
print("ts2 : {}".format(time.mktime(time.strptime(ts2, "%a %b %d %H:%M:%S %Y"))))


# 获取某月日历
calendar1 = calendar.month(2022, 1)
print("以下是2022年1月的calendar:")
print(calendar1)
