import socket

target_host = "127.0.0.1"
target_port = 9991

# buat objek socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# kirim beberapa data
client.sendto(b"AAABBBCCC", (target_host, target_port))

# terima beberapa data
data, addr = client.recvfrom(4096)
print(data.decode())
clinet.close()

