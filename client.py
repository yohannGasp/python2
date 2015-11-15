#!/usr/bin/python3

import socket

sock = socket.socket()
sock.connect(('localhost',9999))
sock.send("123")

data = conn.recv(1024)
conn.close()

print(data)



