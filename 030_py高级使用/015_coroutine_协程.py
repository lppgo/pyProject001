#!/usr/bin/env python
# coding: utf-8


def grep(pattern):
    print("Searching for pattern : {}".format(pattern))
    while True:
        line = yield
        if pattern in line:
            print(line)


search = grep("coroutine")
" 通过next()方法来执行yield表达式,启动一个协程 "
next(search)
# output: Searching for coroutine
search.send("I love you")
search.send("Don't you love me?")
search.send("I love coroutine instead!")
# output: I love coroutine instead!

" 调用一个close()方法来关闭协程 "
search.close()
