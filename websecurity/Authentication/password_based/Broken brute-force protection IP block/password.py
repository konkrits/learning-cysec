#!/usr/bin/python3

with open("username.txt", "w") as f:

	for i in range(1, 150):
		if i % 3:
		     f.write("carlos\n")
		else:
		     f.write("wiener\n")
			
			

