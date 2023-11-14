#! /usr/bin/env pthon
# -*- coding:utf-8 -*-


file = open("mytext.txt", "r")

# content = file.read()

# content = file.readlines()

content = file.readline(10)

file.close()
print(content)



# 打开一个文件以读取内容
file = open("example.txt", "r")

# 逐行读取文件内容并输出
for line in file:
    print(line.strip())  # 使用strip()去除换行符

# 关闭文件
file.close()