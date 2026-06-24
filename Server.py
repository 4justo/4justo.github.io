import socket

HOST = "localhost"
PORT = 12345

# Server setup
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print(f"Server is waiting for client connection on {HOST}:{PORT} ...")

client_socket, addr = server_socket.accept()
print(f"Connection established with {addr}")


# Receive message from client
data = client_socket.recv(1024)
if data:
    print(f"Server received: {data.decode(errors='replace')}")
else:
    print("Server received no data")

# Send reply to client
reply = "Hello from server".encode()
client_socket.sendall(reply)

# Closing connection
client_socket.close()
server_socket.close()

