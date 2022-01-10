#!/usr/bin/python


""" ---------------------- try 处理异常Exception ----------------- """
# while True:
#     try:
#         x = int(input("Please input numbers:"))
#     except (OSError, RuntimeError, ImportError, IOError, TypeError, ValueError, NameError):
#         print("您输入的不是数字，请重新输入!")
#     else:
#         print("{} Yes !".format(x))
#     finally:
#         print("再来!")


""" ------------------------ raise 抛出异常 ------------------------ """
# raise 用来抛出异常
# raise [Exception[, args[, traceback]]]
# x = 10
# if x > 5:
#     raise Exception("x={},x不能大于5!".format(x))

""" ------------------------ 用户自定义异常 ------------------------ """
# 你可以通过创建一个新的异常类来拥有自己的异常，异常类继承自Exception类，可以直接继承或者间接继承。


class Error(Exception):
    """ base class for exception in this module. """
    pass


class InputError(Error):
    """ Exception raised for errors in the input. 

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


class TranslationError(Error):
    """  Raised when an operation attempts a state transition that's not allowed.

    Attributes:
        previous -- state at begining of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """

    def __init__(self, previous, next, message) -> None:
        self.previous = previous
        self.next = next
        self.message = message


# x = 10
# if x > 5:
#     raise InputError(
#         "ErrorCode:{}".format(500), "ErrorMsg: x={},x不能大于5!".format(x))


""" ------------------------ 定义清理行为 Traceback ------------------------ """
# 不管 try 子句里面有没有发生异常，finally 子句都会执行
# 如果一个异常在 try 子句里（或者在 except 和 else 子句里）被抛出，而又没有任何的 except 把它截住，那么这个异常会在 finally 子句执行后被抛出


# def divide(x, y):
#     try:
#         result = x / y
#     except ZeroDivisionError:
#         print("division by zero !")
#     else:
#         print("result = {}".format(result))
#     finally:
#         print("executing finally clause")


# # divide(6, 2)
# divide(6, 0)


""" 
Python 中的 with 语句用于异常处理，封装了 try…except…finally 编码范式，提高了易用性。

with 语句使代码更清晰、更具可读性， 它简化了文件流等公共资源的管理。 

with 语句实现原理建立在上下文管理器之上。

上下文管理器是一个实现 __enter__ 和 __exit__ 方法的类。
"""
with open("myfile.txt") as f:
    data = f.read()  # 以上这段代码执行完毕后，就算在处理过程中出问题了，文件 f 总是会关闭

print(f.close())
