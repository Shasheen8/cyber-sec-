#!/usr/bin/python3

import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host=  socket.gethostname()

port = 5000

clientsocket.connect(('192.168.75.1', port))

message = clientsocket.recv(1024)

clientsocket.close()

print(message.decode('ascii'))