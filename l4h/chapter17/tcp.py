import socket

s = socket.socket()

s.connect(("10.0.2.5", 22))

answer = s.recv(1024)

print (answer)

s.close
