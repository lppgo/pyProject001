#!/usr/bin/env python

import sys
import socket

''' 创建socket对象 '''
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

''' 获取本地主机名,port '''
hostname=socket.gethostname()
port=9999

''' 连接服务端，指定主机和端口 '''
s.connect((hostname,port))

''' 接收数据 '''
bufsize=1024
msg=s.recv(bufsize)
s.close()

print(msg.decode("utf-8"))
