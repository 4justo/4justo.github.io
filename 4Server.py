import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(5)

print("Server running...")

while True:
    client_socket, addr = server_socket.accept()
    print("Connected:", addr)

    client_socket.send(b"Connected to server")
    client_socket.close()