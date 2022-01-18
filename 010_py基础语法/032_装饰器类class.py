#!/usr/bin/env python
# coding: utf-8

from functools import wraps


class logit(object):
    def __init__(self, logfile="out.log"):
        self.logfile = logfile

    def __call__(self, func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + "was called"
            print("log_string : {}".format(log_string))
            with open(self.logfile, "a") as f:
                f.write(log_string + "\n")
            # 现在，发送一个通知
            self.notify()
            return func(*args, **kwargs)

        return wrapped_function

    def notify(self):
        # logit 只打印日志
        pass


""" 这个实现有一个附加优势，在于比嵌套函数的方式更加整洁，而且包裹一个函数还是使用跟以前一样的语法 """


@logit
def myfunc1():
    pass


""" 现在，我们给logit创建子类，来添加email的功能 """


class email_logit(logit):
    """
    一个logit的实现版本，可以在函数调用时发送email给管理员
    """

    def __init__(self, email="admin@myproject.com", *args, **kwargs):
        self.email = email
        super(email_logit, self).__init__(*args, **kwargs)

    def notify(self):
        # 发送一封email到self.email
        # 这里就不做实现了
        pass


@email_logit
def myfunc2():
    pass


"""
从现在起，@email_logit将会和@logit产生同样的效果，但是在打日志的基础上，还会多发送一封邮件给管理员
"""
