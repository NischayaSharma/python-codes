import socket;
import sys;
import thread;

try:
    s = socket.socket();
    port = 12345;
    s.bind(('', port));
    s.listen(5);
    numOfClients = 0;

    def main(c):
        global numOfClients;
        while True:
            rcvdData = c.recv(1024).decode();
            print "S:",rcvdData;
            sendData = raw_input("N: ");
            c.send(sendData.encode());
            if(sendData == "Bye" or sendData == "bye"):
                break;
        c.close();

    while 1:
        c, addr = s.accept();
        print "Socket Up and running with a connection from",addr;
        thread.start_new_thread(main,(c,));

except KeyboardInterrupt:
    print "Closing Connection and freeing the port."
    c.close();
    sys.exit();
