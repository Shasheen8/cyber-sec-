#TCP server using python 
#!/usr/bin/python3

import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#host ip address
host = socket.gethostname()
port = 5000

serversocket.bind( (host , port))

serversocket.listen(3)

#starting a connection 
while True:
    clientsocket, address = serversocket.accept()

    print(" recieve connection from:  %r"  % str(address))

    message= 'Thank you for connecting to the server ' + "\r\n"
    clientsocket.send(message.encode('ascii'))

    clientsocket.close()