import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 5000))
server.listen(1)

print("Server is waiting for connection...")

conn, address = server.accept()
print("Client connected:", address)

while True:

    message = conn.recv(1024).decode()

    if message.lower() == "exit":
        break

    print("Client:", message)

    reply = input("Server: ")
    conn.send(reply.encode())

    if reply.lower() == "exit":
        break

conn.close()
server.close()