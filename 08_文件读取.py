#! /usr/bin/env pthon
# -*- coding:utf-8 -*-


file = open("./mytext.txt", "r")

# content = file.read()

# content = file.readlines()

content = file.readline(10)

file.close()
print(content)
