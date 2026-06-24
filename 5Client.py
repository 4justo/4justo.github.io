import socket
import time

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)

print("Server is waiting for client connection...")

client_socket, addr = server_socket.accept()
print(f"Connection established with {addr}")

# Simulate network delay
time.sleep(5)

client_socket.send(b'Hello from server')

client_socket.close()
server_socket.close()