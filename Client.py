import socket

HOST = "localhost"
PORT = 12345

# Client setup
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Send message to server
message = "Hello from client".encode()
client_socket.sendall(message)

# Receive reply from server
data = client_socket.recv(1024)
print(f"Client received: {data.decode(errors='replace')}")

# Closing connection
client_socket.close()

