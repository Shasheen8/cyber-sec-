#!/usr/bin/python3

import socket 

s =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = input ('Please enter the IP to scan : ')
port = str(input('Please enter the port to scan : '))

def portScan(port):
    if s.connect_ex((ip,port)):
        print("the port is closed")
    else:
        print("The port is closed")

portScan(port) 