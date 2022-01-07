#! /usr/bin/env python
# -*- coding:utf-8 -*-

import time
import time as t            # alias
from time import localtime  # 只导入time包的localtime功能
# from time import *        # 导入time的所有功能，省去time

print(time.localtime())
print(t.localtime())
print(localtime())


# module 模块是一个包含所有你定义的函数和变量的文件，其后缀名是.py
# module 模块可以被别的程序引入，以使用该模块中的函数


"""
import 与 from...import

在 python 用 import 或者 from...import 来导入相应的模块。

将整个模块(module)导入，格式为: import module

从某个模块中导入某个函数, 格式为: from module import somefunction

从某个模块中导入多个函数, 格式为: from module import firstfunc, secondfunc, thirdfunc

将某个模块中的全部函数导入，格式为: from module import *

"""
