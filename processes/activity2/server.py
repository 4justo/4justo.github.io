import socket
import threading

def handle_client(client_socket, addr):
    thread_id = threading.get_ident()
    request = client_socket.recv(1024)
    print(f"Thread {thread_id} handling client {addr}: {request.decode()}")
    client_socket.send(b'Hello from server')
    client_socket.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12345))
server.listen(5)
print("Server listening on localhost:12345")

while True:
    client_sock, addr = server.accept()
    active_threads = threading.active_count()
    print(f"Connection from {addr} | Active threads: {active_threads}")
    client_thread = threading.Thread(target=handle_client, args=(client_sock, addr))
    client_thread.start()