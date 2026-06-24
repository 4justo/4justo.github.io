import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)

print("Waiting for client...")

client_socket, addr = server_socket.accept()

message = client_socket.recv(1024)
print("Client says:", message.decode())

client_socket.send(b"Message received successfully")

client_socket.close()
server_socket.close()