#!/usr/bin/env python
# coding: utf-8

""
"""
  ------------------- python单元测试 -----------------------

1: unittest包括python标准库中的测试模型
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
