#!/usr/bin/python3

import socket

sock = socket.socket()
sock.bind(('',9999))
sock.listen(1)
conn, addr = sock.accept()

print('Client adress: ', addr)

data = conn.recv(1024)
print(data)
#conn.send("hello client")

conn.close()


