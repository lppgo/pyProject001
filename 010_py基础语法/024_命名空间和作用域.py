#!/usr/bin/env python

""" 全局变量和局部变量 """

total = 0  # 这是一个全局变量


''' ---------------- 注意: 不可变类型和可变类型在函数中是传值还是传引用？------------------- '''


def sum(arg1, arg2):
    total = arg1 + arg2  # total在这里是局部变量.
    print("函数内是局部变量 : ", total)
    return total  # 返回2个参数的和."


sum(10, 20)
print("函数外是全局变量 : ", total)


''' -------------------- global和nonlocal关键字 ------------------- '''
""" 
当内部作用域想修改外部作用域的变量时，就要用到 global 和 nonlocal 关键字了

如果要修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量则需要 nonlocal 关键字了

"""
num = 1


def fn1():
    global num  # 用global关键字声明
    print("(1) num={}".format(num))
    num = 123
    print("(2) num={}".format(num))
    return num


fn1()
print("(3) num={}".format(num))


def outer():
    a = 10

    def inner():
        nonlocal a
        a = 110
        print("(1) a={}".format(a))

    inner()
    print("(2) a={}".format(a))


outer()


# -----------------------------------
b = 10


def test():
    global b
    b = b + 1
    print(b)


test()
