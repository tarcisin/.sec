import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("google.com", 80))
client.send(b"Bonju")
client.recv(1024)