#!/usr/bin/env python

import sys
import socket

''' 创建socket对象 '''
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

''' 获取本地主机名 '''
hostname=socket.gethostname()
port=9999

''' 绑定端口 '''
s.bind((hostname,port))

''' 设置最大连接数，超过后排队 '''
s.listen(5)

while True:
    ''' 接收客户端连接 '''
    print("server wait for accept ...")
    socket_client,addr=s.accept()
    print("连接地址:{}".format(str(addr)))
    msg='欢迎访问菜鸟教程！'+ "\r\n"
    socket_client.send(msg.encode("utf-8"))
    socket_client.close()
