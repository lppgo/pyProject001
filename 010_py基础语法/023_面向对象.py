#!/usr/bin/python

class People:
    # 基本属性
    name = ""
    age = 0
    # 类的私有属性，私有属性在类的外部无法直接访问
    __weight = 0

    # 构造函数
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    # 类的方法
    def speak(self):
        print("{}说: 我的age是:{},我的体重是:{} KG".format(
            self.name, self.age, self.__weight))


peeter = People("peeter", 27, 65)
print(peeter.name)
# print(peeter.__weight)
peeter.speak()

""" ------------------- 继承 Inherit ------------------- """


class Student(People):
    """ 单继承示例 """
    grade = ""

    def __init__(self, n, a, w, g):
        # 调用父类的构造
        People.__init__(self, n, a, w)
        self.grade = g

    # override覆写父类的方法
    def speak(self):
        print("{}说: 我是一名student，我的grade是:{},我的age是:{}".format(
            self.name, self.grade, self.age))


stu1 = Student("jiojio", 18, 60, g='A')
# 方法已被子类覆写
stu1.speak()
# super() 函数是用于调用父类(超类)的一个方法
super(Student, stu1).speak()


class Speaker():
    name = ""
    topic = ""

    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def speak(self):
        print("{}说: 我是一名演说家，我的演讲主题是:{}".format(self.name, self.topic))

# 多继承
# 需要注意圆括号中父类的顺序，若是父类中有相同的方法名，而在子类使用时未指定，python从左至右搜索 即方法在子类中未找到时，从左到右查找父类中是否包含方法


class StudentSpeaker(Speaker, Student):
    """ 学生演讲家(多继承示例) """
    name = ""

    def __init__(self, n, a, w, g, t):
        Student.__init__(self, n, a, w, g)
        Speaker.__init__(self, n, t)


stuSpeaker1 = StudentSpeaker("lucas", 18, 65, "A++", "如何学习?")
stuSpeaker1.speak()
