#!/usr/bin/python

""" 
       ----------------------- 函数参数 -------------------------
1: 必需参数 
        必需参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样

2: 默认参数
        调用函数时，如果没有传递参数，则会使用默认参数。以下实例中如果没有传入 age 参数，则使用默认值

3: 关键字参数 
        关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值;
        使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值;


4: 不定长参数
        加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数
        加了两个星号 ** 的参数会以字典的形式导入
"""


# ----------- 函数必需参数 ------------
def printme_1(str):
    "打印任何传入的字符串"
    print(str)
    return


printme_1("hi")


# ---------- 默认参数 -----------------
def printme_2(str="lucas"):
    print(str)
    return


printme_2()


# -------------- 关键字参数 -------------
def printme_3(str):
    "打印任何传入的字符串"
    print(str)
    return


printme_3(str="菜鸟教程")


# ------------- 不定长参数 ---------------
def printme_3(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vartuple)


printme_3(70, 60, 50)


def printme_4(arg1, **vartuple):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vartuple)


printme_4(70, b=60, c=50)


#  ------------ 强制位置参数 -------------------
""" 
Python3.8 新增了一个函数形参语法 / 用来指明函数形参必须使用指定位置参数，不能使用关键字参数的形式。

在以下的例子中，形参 a 和 b 必须使用指定位置参数，c 或 d 可以是位置形参或关键字形参，而 e 和 f 要求为关键字形参:

"""


def f(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)
