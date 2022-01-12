#! /usr/bin/env python
# -*- coding:utf-8 -*-


def welcom(name):
    print("Welcom %s" % (name))


def area(weigh, heigh):
    return weigh * heigh


welcom("lucas")

print(area(10, 20))

a = 88
print("a:%d " % a, "addr: %d" % (id(a)))
a = "py中，变量是没有类型的，变量a仅仅是一个对象的引用(指针)"
print(a)
print("a     addr: %d" % (id(a)))


""" 
    ----------------- 可更改(mutable)与不可更改对象(immutable) --------------------- 

不可变类型: Number,String,Tuple
        变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变 a 的值，相当于新生成了 a ;

可变类型: List,Set,Dict
        变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了
"""

""" 
    ----------------- python 函数的参数传递: -------------------------------

不可变类型: 类似 C++ 的值传递，如整数、字符串、元组。如 fun(a)，传递的只是 a 的值，没有影响 a 对象本身。如果在 fun(a) 内部修改 a 的值，则是新生成一个 a 的对象 ;

可变类型: 类似 C++ 的引用传递，如 列表，字典。如 fun(la)，则是将 la 真正的传过去，修改后 fun 外部的 la 也会受影响 ;

python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象 ;

 """

# 函数参数传不可变对象


def change(a):
    print(id(a))   # 指向的是同一个对象
    a = 10
    print(id(a))   # 一个新对象


a = 1
print(id(a))
change(a)
print(id(a))


# 函数参数传可变对象
def changeme(mylist):
    "修改传入的列表"  # DocString
    mylist.append([1, 2, 3, 4])
    print("函数内取值: ", mylist)
    return


mylist = [10, 20, 30]
print(id(mylist))
changeme(mylist)
print("函数外取值: ", mylist)
print(id(mylist))
print("打印函数的DocString:%s" % (changeme.__doc__))


""" --------------- lambda 匿名函数 ----------------------- """
def sum(arg1, arg2): return arg1 + arg2


print("相加后的值为 : ", sum(10, 20))
print("相加后的值为 : ", sum(20, 20))
