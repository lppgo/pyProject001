#! /usr/bin/env python
# -*- coding:utf-8 -*-

if __name__ == "__main__":
    print("该程序块仅在该模块自身运行时执行")
else:
    print("在外部模块运行!")


def printdata(data):
    print("data:", data)
