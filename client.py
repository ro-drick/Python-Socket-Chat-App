import socket

DEST_IP = socket.gethostbyname(socket.gethostname())
DEST_PORT = 12345
ENCODER = "utf-8"
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((DEST_IP, DEST_PORT))

while True:
    message = client_socket.recv(1024).decode(ENCODER)
    if message == "quit":
        client_socket.send("quit".encode(ENCODER))
        print("Ending chat!\n")
        break
    else:
        print(f"\n{message}")
        message = input("Client: ")
        client_socket.send(message.encode(ENCODER))
client_socket.close()
