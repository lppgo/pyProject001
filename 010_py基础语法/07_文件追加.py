#! /usr/bin/env pthon
# -*- coding:utf-8 -*-


# -------文件写入--------
#   追加写入, a--append------
file = open("mytext.txt", "a")
file.write("\n\nThis is append new line.")
file.close()
