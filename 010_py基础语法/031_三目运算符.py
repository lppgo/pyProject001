#!/usr/bin/env python
# coding: utf-8

""
"""
#如果条件为真，返回真 否则返回假
condition_is_true if condition else condition_is_false

#(返回假，返回真)[真或假]
(if_test_is_false, if_test_is_true)[test]

"""


is_fat = True
a = "true" if is_fat else "false"
print("a = {}".format(a))


res = ("C++", "Python")[True]
print("res = {}".format(res))
