import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

client_socket.send(b"Hello Server")

reply = client_socket.recv(1024)
print("Server Reply:", reply.decode())

client_socket.close()