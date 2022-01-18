#! /usr/bin/env python
# -*- coding:utf-8 -*-


fname = "111.txt"

# try:
#     file = open(fname, "r+")
#     print(file.read())
#     # print(file.readline())
#     # print(file.readlines())
#     # print(file.read(10))
# except Exception as err:
#     print("open Error:", err)
#     opt = input("do you want to create this file (yes/no):")
#     if opt == "yes":
#         file = open(fname, "w")
#         print(fname, "is created successed!")
#     else:
#         print("exit ...")
#         pass
# else:
#     file.write("hi: try !\n")
#     file.close()


# 迭代一个文件对象，然后读取每行
f = open(fname, "r+")
for line in f:
    print(line)


# f.tell() 返回文件对象当前所处的位置, 它是从文件开头开始算起的字节数。
print(f.tell())


# f.seek() 改变文件当前的位置, 可以使用 f.seek(offset, from_what) 函数
# from_what 的值, 如果是 0 表示开头, 如果是 1 表示当前位置, 2 表示文件的结尾


print(f.seek(10, 0))
print(f.tell())

f.close()


""" 当处理一个文件对象时, 使用 with 关键字是非常好的方式。在结束后, 它会帮你正确的关闭文件。 而且写起来也比 try - finally 语句块要 

上下文管理器: ContextManager
- 上下文管理器允许你在有需要的时候，精确地分配和释放资源;
- 想象下你有两个需要结对执行的相关操作，然后还要在它们中间放置一段代码;
- with ;
- 上下文管理器的一个常见用例，是资源的加锁和解锁，以及关闭已打开的文件;

"""
with open(fname, "r") as f2:
    print(f2.read())

f2.close()
