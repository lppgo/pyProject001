#!/usr/bin/env python
# coding: utf-8

""" """
""" 进程池pool 
如果要启动大量的子进程，可以用进程池(Pool)的方式批量创建子进程;

"""

from multiprocessing import Pool
import os, time, random


def run_task(name):
    print("Run Task : %s " % name)
    t_start = time.time()
    time.sleep(random.random())
    t_end = time.time()
    print("Task %s run %.2f sec " % (name, t_end - t_start))


if __name__ == "__main__":
    print("Parent %s Process is running ... " % (os.getpid()))

    # Pool 类表示一个工作进程池
    p = Pool(5)
    for i in range(5):
        p.apply_async(run_task, args=(i,))
    print("All subProcess will running ... ")

    p.close()  # 阻止后续任务提交到进程池，当所有任务执行完成后，工作进程会退出
    p.join()  # 等待工作进程结束。调用 join() 前必须先调用 close() 或者 terminate()
    print("All sub Process running completed ...")
