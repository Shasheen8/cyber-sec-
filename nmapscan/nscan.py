#!/usr/bin/python3

import nmap

scanner = nmap.PortScanner()

print ("Welcome, nmap automation tool")
print ("<----------------------------------->")


ip_addr = input("Please enter the IP address you want to scan: ")
print (" The IP address you entered is: ", ip_addr)
type(ip_addr)

resp = input("""\nPlease enter the type of scan you want to perform 
                    1)SYN ACK Scan 
                    2)UDP Scan 
                    3)Comprehensive Scan\n""")
print ("You have selected the option: ", resp)


if resp == '1':
    print ("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS')
    print (scanner.scaninfo())
    print ("Ip address Status: ", scanner[ip_addr].state())
    print (scanner [ip_addr].all_protocols())
    print ("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif resp == '2' :
    print ("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr,  '1-1024' , ' -v  -sU ')
    print (scanner.scaninfo())
    print ("Ip address Status: ", scanner[ip_addr].state())
    print (scanner [ip_addr].all_protocols())
    print ("Open Ports: ", scanner[ip_addr]['udp'].keys())
elif resp == '3' :
    print ("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr,  '1-1024' , ' -v  -sS -sV -sC -A -0')
    print (scanner.scaninfo())
    print ("Ip address Status: ", scanner[ip_addr].state())
    print (scanner [ip_addr].all_protocols())
    print ("Open Ports: ", scanner[ip_addr]['udp'].keys())
elif resp >= '4':
    print ("Enter the valid option from the above. ")
