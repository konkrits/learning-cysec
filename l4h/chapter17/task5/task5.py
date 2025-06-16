import socket

ports = [21,22.25,3306]

for i in range (0,4):

   s = socket.socket()

   ports = ports[i]

   print ("this is info for port:")

   print (ports)

   s.connect (("10.0.2.5", ports))

   answer = s.recv(1024)

   print (answer)

   s.close 
