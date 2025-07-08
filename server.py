import socket

HOST_ADDRESS = socket.gethostbyname(socket.gethostname())
HOST_PORT = 12345
BYTE_SIZE = 1024
ENCODER = "utf-8"

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST_ADDRESS, HOST_PORT))

server_socket.listen()
print("Server waiting for connection...\n")

client_socket, client_addr = server_socket.accept()

client_socket.send("Connected to server successfully...\n".encode(ENCODER))
while True:
    message = client_socket.recv(1024).decode(ENCODER)
    if message == "quit":
        client_socket.send("quit".encode(ENCODER))
        print("\nEnding chat...")
        break
    else:
        print(f"\n{message}")
        message = input("Server: ")
        client_socket.send(message.encode(ENCODER))
server_socket.close()
client_socket.close()
