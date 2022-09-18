#! /usr/bin/env python
# -*- coding:utf-8 -*-

# -------------------zip------------------------
# zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象，这样做的好处是节约了不少的内存。
# 我们可以使用 list() 转换来输出列表。
# 如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。

a = [1, 2, 3]
b = [4, 5]
c = [4, 5, 6, 7, 8]
ziped = zip(a, b)  # zip 压缩，返回一个对象
print(ziped)  # <zip object at 0x7f0d83540f00>
print(list(ziped))  # list() 转为一个list列表 [(1, 4), (2, 5)]

print(list(zip(a, c)))  # 元素个数与最短的列表一致  [(1, 4), (2, 5), (3, 6)]

print("list(zip(a,a,b))=", list(zip(a, a, b))) # list(zip(a,a,b))= [(1, 1, 4), (2, 2, 5)]

# zip()压缩， zip(*)解压
a1, a2 = zip(*zip(a, b))
print("a1:", a1, list(a1))
print("a2:", a2, list(a2))


# -------------------lambda------------------------


def func1(x, y): return x + y


result1 = func1(2, 5)
print(result1)  # 7

# func2=lambda x,y:x+y


def func2(x, y): return x + y


print(func2(2, 3))  # 5

# -------------------map------------------------
result = list(map(func1, [1], [2]))
print(result)  # [3]


result2 = list(map(func1, [1, 3], [2, 8]))
print(result2)  # [3, 11]
