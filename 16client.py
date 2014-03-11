#!/usr/bin/env python
# -*- coding: utf-8 -*-
# client.py
import socket
# ここを変更
host = '127.0.0.1'
port = 8765

clientsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsock.connect((host, port))

while True:
    print("メッセージを入力してください")
    send_message = raw_input()

    print '待機中'
    clientsock.sendall(send_message)
    rcvmsg = clientsock.recv(1024)
    print '受信メッセージ -> %s' % (rcvmsg)

clientsock.close()
