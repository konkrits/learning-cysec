#!/usr/bin/python3

import socket

ports = [21,22,25,3306]

for i in range (0,4):

	s = socket.socket()

		ports = port[i]

		print ("this is banner for port : ")

		print (ports)

		s.connect (("

		answer = s.recv (1024)

		print (answer)

		s.close()
