#!/usr/bin/env python

# coding: utf-8
import socket

# 创建一个TCP连接
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 连接服务端
s.connect(("127.0.0.1", 9999))
# 接收来自服务端的信息
print(s.recv(1024).decode("utf-8"))
# 发送数据给服务端
for x in [b"Python", b"PHP"]:
    s.send(x)
    print(s.recv(1024).decode("utf-8"))
# 发送断开连接命令
s.send(b"exit")
s.close()
