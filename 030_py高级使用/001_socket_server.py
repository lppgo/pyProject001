#!/usr/bin/env python

# coding: utf-8
import socket, threading

# 创建一个TCP连接
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定IP和端口
s.bind(("127.0.0.1", 9999))
# 开始监听客户端连接
# 传入的参数指定等待连接的最大数量
s.listen(3)
# 输出提示语
print("Server is running on %s:%s" % ("127.0.0.1", 9999))
print("Waiting for connection...")


def tcp_link(sock, addr):
    print("Accept new connection from %s:%s..." % addr)  # 参数addr是一个tuple
    sock.send(b"Welcome!")  # 发送问候语给客户端
    while True:
        r = sock.recv(1024)
        if not r or r.decode("utf-8") == "exit":  # 结束连接指令
            break
        # 输出客户端发来的信息，注意元组拼接
        msg = addr + (r.decode("utf-8"),)
        print("%s:%s : %s" % msg)
        # 回复客户端
        sock.send(("you say: %s" % r.decode("utf-8")).encode("utf-8"))
    sock.close()
    print("Client %s:%s is closed." % addr)


while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    print(addr)  # ('127.0.0.1', 62090)
    # 创建新线程来处理TCP连接:
    # 每个连接都必须创建新线程（或进程）来处理，否则，单线程在处理连接的过程中，无法接受其他客户端的连接
    t = threading.Thread(target=tcp_link, args=(sock, addr))
    t.start()
