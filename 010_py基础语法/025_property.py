#!/usr/bin/env python


"""
  ------------ @property  ----------------
Python内置的@property就是负责把一个方法变成属性调用。
此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值
"""


class Student(object):
    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        if value > 100:
            value = 100
        if value < 0:
            value = 0
        self.__score = value


s = Student()
s.score = 199  # setter
print(s.score)  # getter

print(s)
print(repr(s))


""" 
  ------------ 定制类 ------------
__slots__：限制实例的属性
__len__()：自定义返回长度
__str__()：当尝试使用print打印类的时候，自定义返回类的内容。
    因为默认打印出一堆<__main__.Student object at 0x109afb190>，不好看
    
__repr__()：与__str__()类似，当直接敲变量Student('yjc')不用print的时候，会自动调用该方法
__getattr__()：默认调用类里不存在的属性时，会报错。通过该方法，可以动态返回一个属性
__call__()：通过覆写该方法，可以将实例像方法那样直接调用
"""
