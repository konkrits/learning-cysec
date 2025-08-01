#!/usr/bin/python3

with open('listpass.txt', 'r') as file:
    lines = file.readlines()

with open('password.txt', 'w') as f:
    for i, pwd in enumerate(lines):
        f.write(pwd.strip('\n') + '\n')  # Write the original password
        if (i + 1) % 2 == 0:  # After every 3rd password
            f.write('peter\n')  # Write 'peter' on a new line

 
