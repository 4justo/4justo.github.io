import socket
import threading

counter = 0
counter_lock = threading.Lock()

def handle_client(client_socket):
    global counter
    request = client_socket.recv(1024)
    with counter_lock:
        counter += 1
        current_count = counter
    print(f"Received: {request.decode()} | counter={current_count}")
    client_socket.send(b'Hello from server')
    client_socket.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12345))
server.listen(5)
print("Server listening on localhost:12345")

while True:
    client_sock, addr = server.accept()
    print(f"Connection from {addr}")
    client_thread = threading.Thread(target=handle_client, args=(client_sock,))
    client_thread.start()