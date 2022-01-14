#!/usr/bin/env python

""" """
"""
python  mysql
1：通过fork()系统调用，就可以生成一个子进程
Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊。普通的函数调用，调用一次，返回一次，但是fork()调用一次，返回两次，
因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回。

2：子进程永远返回0，而父进程返回子进程的ID。
这样做的理由是，一个父进程可以fork出很多子进程，所以，父进程要记下每个子进程的ID，而子进程只需要调用getppid()就可以拿到父进程的ID。

3: multiprocessing
虽然fork()调用无法在Windows调用，但Python也提供了跨平台的多进程支持。使用multiprocessing即可创建跨平台多进程：
"""
import os

print("Process {} start ...".format(os.getpid()))

pid = os.fork()

if pid == 0:  # 子进程返回 0
    print("I am child Process {} , my parent is {} ".format(os.getpid(), os.getppid()))
else:  # 父进程返回子进程 id
    print("I am parent Process {}, my child Process is {}".format(os.getpid(), pid))

# Process 7429 start ...
# I am parent Process 7429, my child Process is 7433
# I am child Process 7433 , my parent is 7429

""" 进程池pool 
如果要启动大量的子进程，可以用进程池(Pool)的方式批量创建子进程;

"""
