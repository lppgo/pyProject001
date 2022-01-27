#!/usr/bin/env python
# coding: utf-8

""
"""
  ------------------- python单元测试 -----------------------

1: unittest包括python标准库中的测试模型

2: py.test 
    相比于Python标准的单元测试模块,py.test是一个没有模板的选择
    pip install pytest
    
3: Hypothesis
    pip install hypothesis
    
4: tox 
    是自动化测试管理和针对多种解释器配置的测试工具
    pip install tox
    
5: mock
    unittest.mock是Python中用于测试的一个库
    pip install mock
"""

import unittest


def func(x):
    return x + 1


class MyTest(unittest.TestCase):
    """对函数func 进行unittest"""

    def test(self):
        self.assertEqual(func(3), 4)


#
unittest.main()
