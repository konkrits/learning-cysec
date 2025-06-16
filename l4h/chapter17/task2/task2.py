import socket

s = socket.socket()

i = input("enter the ip:\n")
p = int(input("enter the port:\n"))

s.connect((i, p))

answer = s.recv(1024)

print (answer)

s.close

