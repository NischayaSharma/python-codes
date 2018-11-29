import socket;

s = socket.socket();
port = 12345;
s.bind(('', port));
s.listen(5);
clients = [];
addr = [];
while True:
    c, address = s.accept();
    clients.append(c);
    addr.append(address);
    print "Socket Up and running with a connection from",addr;
    for i in range(len(clients)):
        rcvdData = clients[i].recv(1024).decode();
    print "S:",rcvdData;
    sendData = raw_input("N: ");
    for i in range(len(clients)):
        clients[i].send(sendData.encode());
    if(sendData == "Bye" or sendData == "bye"):
        break;
c.close();
