import socket;

s = socket.socket();
print "Socket successfully created";
port = 12345;
s.bind(('', port));
print "socket binded to %s" %(port);
s.listen(5);
print "socket is listening";
c, addr = s.accept();
print 'Got connection from', addr;
while True:
    rcvdData = c.recv(1024).decode();
    print "S:",rcvdData;
    sendData = raw_input("N: ");
    c.send(sendData.encode());
    if(sendData == "Bye" or sendData == "bye"):
        break;
c.close();
