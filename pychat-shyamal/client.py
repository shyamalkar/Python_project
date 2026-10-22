import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5000))

print("Connected to server!")

while True:

    message = input("Client: ")
    client.send(message.encode())

    if message.lower() == "exit":
        break

    reply = client.recv(1024).decode()
    print("Server:", reply)

    if reply.lower() == "exit":
        break

client.close()

