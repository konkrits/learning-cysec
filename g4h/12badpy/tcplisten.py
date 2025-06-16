#!/usr/bin/python3

import socket

TCP_IP="10.0.2.15"
TCP_PORT=5555
BUFFER_SIZE=100

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((TCP_IP, TCP_PORT))
s.listen (1)

conn, addr=s.accept()
print (f"connection addres: {addr}")

while 1:

	data=conn.recv(BUFFER_SIZE)
	if not data:break
	print (f"receive data {data}")
	conn.send(data)

conn.close
