import socket

def banner_grab(host, port):
    try:
        # Create a socket connection
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        sock.connect((host, port))
        sock.send(b'HEAD / HTTP/1.1\r\n')  # Send a simple HTTP request to get a banner
        banner = sock.recv(1024).decode('utf-8', errors='ignore')  # Try to receive the banner
        if banner:
            return banner.strip()
        else:
            return None
    except (socket.timeout, socket.error):
        return None
    finally:
        sock.close()

def main():
    host = input("Enter the host (IP or domain name): ")
    
    print(f"Scanning ports 1-1000 on {host}...")
    
    for port in range(1, 1001):
        banner = banner_grab(host, port)
        if banner:
            print(f"Port {port}: {banner}")
        else:
            print(f"Port {port}: No banner found or connection failed")

if __name__ == "__main__":
    main()
