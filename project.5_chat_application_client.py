import socket

HOST = '127.0.0.1'  # Server IP
PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

while True:
    msg = input("You: ")
    client_socket.send(msg.encode())
    data = client_socket.recv(1024).decode()
    print(f"Server: {data}")

client_socket.close()
