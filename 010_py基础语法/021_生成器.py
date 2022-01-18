#!/usr/bin/python

""
""" 
      ---------------- 生成器 generator ---------------

在python种，使用了yeild的函数被称为生成器；

跟普通函数不同的是，生成器geneartor 是一个返回迭代器的函数，只能用于迭代操作；

在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行。

调用一个生成器函数，返回的是一个迭代器对象;

在 for 循环中会自动调用 next();

generator函数和普通函数的执行流程不一样。
普通函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行;

"""

import sys


def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if counter >= n:
            return
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成

# while True:
#     try:
#         print(next(f))
#     except StopIteration:
#         sys.exit()

# for x in f:
#     print(x)

""" 由生成器返回的迭代器，可使用__next__()来获取下一个值 """
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
