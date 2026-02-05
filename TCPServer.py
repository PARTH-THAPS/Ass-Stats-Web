import json
import socket

HOST = '127.0.0.1'
PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((HOST, PORT))
server_socket.listen(1)

print("Server waiting for connection...")

conn, addr = server_socket.accept()
print(f"Connected by {addr}")

data = conn.recv(1024).decode("utf-8")

url_parts = json.loads(data)

full_url = (
    f"{url_parts['scheme']}://"
    f"{url_parts['netloc']}"
    f"{url_parts['path']}"
)

if url_parts.get("query"):
    full_url += f"?{url_parts['query']}"

if url_parts.get("fragment"):
    full_url += f"#{url_parts['fragment']}"

print("Reconstructed URL:", full_url)

conn.close()
server_socket.close()
