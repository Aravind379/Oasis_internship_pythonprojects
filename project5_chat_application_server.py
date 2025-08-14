import socket


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))  
server_socket.listen(1)

print("Server is waiting for a connection...")
conn, addr = server_socket.accept()
print(f"Connected by {addr}")

while True:
    client_msg = conn.recv(1024).decode()
    if client_msg.lower() == "bye":
        print("Client has ended the chat.")
        break
    print(f"Client: {client_msg}")

    server_msg = input("You: ")
    conn.send(server_msg.encode())
    if server_msg.lower() == "bye":
        print("You ended the chat.")
        break

conn.close()
server_socket.close()
