#! /usr/bin/env python
# -*- coding:utf-8 -*-

condition = 1

tk = 10

print("while 循环")
while condition <= tk:
    print(condition)
    condition = condition + 1

# while True:
#     print("loop algorithm")

# example_list = [1, 2, 3, 4, 5]
# for i in example_list:
#     print(i)

print("for循环")
example_list = ["a", "b", "c"]
for i in example_list:
    print(i)
    print(i)
    print(i)

print("for range循环")
for i in range(1, 7, 2):
    print(i)

print("end...")


a_list = [1, 2, 2, 3, 1, 9, 9, 6, 8, 9, 12]

# for i in a_list:
#     print(i)

for i in range(len(a_list), 12):
    print(i)
