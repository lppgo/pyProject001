#! /usr/bin/env pthon
# -*- coding:utf-8 -*-

# -------文件创建，写入-------
mytext = "This is my first test.\nThis is next line.\nThis is end line."

#    写入文件,w--write------
file = open("./mytext.txt", "w")
file.write(mytext)
file.close()
