# !/usr/bin/env python3

import sys

# 引入sys模块

""" 
 --------------- iterator 迭代器 --------------------

迭代器是一个可以记住遍历位置的对象
迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问结束，迭代器只会前进，不会后退

iter()
next()

StopIteration 异常用于标识迭代的完成，防止出现无限循环的情况

 """

list1 = ["C", "C++", "Ruby", "python", "Java", "Go", "Rust"]

it = iter(list1)  # 创建一个迭代器对象

# (1) next()  输出迭代器的下一个元素
# print(next(it)) # 输出迭代器的下一个元素
# print(next(it)) # 输出迭代器的下一个元素
# print(next(it)) # 输出迭代器的下一个元素

# (2) for 循环遍历迭代器对象
for x in it:
    print(x)


# (3) while 循环遍历迭代器
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit()

""" 
    ---------- 把类作为一个迭代器 ---------------
__iter__() 返回一个特殊的迭代器对象,这个迭代器对象实现了__next__() 方法，并通过 StopInteration 异常标识迭代的完成；
__next__() 会返回下一个迭代器对象

"""
# 创建一个返回数字的迭代器，初始值为1，逐步递增1


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration  # StopIteration 异常用于标识迭代的完成，防止出现无限循环的情况


mynum = MyNumbers()
myiter = iter(mynum)

for x in myiter:
    print(x)
    if x >= 10:
        break

for x in myiter:
    print(x)

""" 由生成器返回的迭代器，可使用__next__()来获取下一个值 """
print(myiter.__next__())
print(myiter.__next__())
print(myiter.__next__())



