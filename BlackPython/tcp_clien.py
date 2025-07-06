#tcp_clien

import socket

target_host = "www.example.com"
targe_port = 80

# buat objek socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# klien konek
client.connect((target_host, targe_port))

# mengirim beberapa data
client.send(b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")

# menerima beberapa data
response = client.recv(4096)

print(response.decode())
client.close()