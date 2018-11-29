import socket;
import sys;
import thread;
try:
    numOfThreads = 0;
    s = socket.socket();
    port = 12345;
    s.bind(('', port));
    s.listen(5);
    def main():
        global numOfThreads;
        numOfThreads += 1;
        print "Entering main."
        c, addr = s.accept();
        print "Socket Up and running with a connection from",addr;
        while True:
            rcvdData = c.recv(1024).decode();
            print "S:",rcvdData;
            sendData = raw_input("N: ");
            c.send(sendData.encode());
            if(sendData == "Bye" or sendData == "bye"):
                break;
        c.close();
        numOfThreads -= 1;
    thread.start_new_thread(main,());
    while 1:
        pass;
    print "Exited Thread";
except:
    print "Closing Connection and freeing the port."
    c.close();
    sys.exit();
