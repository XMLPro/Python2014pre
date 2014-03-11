#!/usr/bin/env python
# -*- coding: utf-8 -*-
#server.py
import socket
# ここを書き換え
host = '127.0.0.1'
port = 8765

serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversock.bind((host,port))
serversock.listen(1)
print '接続待機中'

connection, client_address = serversock.accept()

while True:
    rcvmsg = connection.recv(1024)
    print '受信メッセージ -> %s' % (rcvmsg)

    print 'テキストを入力してください'
    s_msg = raw_input()
    print '待機中'

    connection.sendall(s_msg) 

connection.close()
