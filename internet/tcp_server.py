# now,we create a simple server,it can be connected,and return a msg
import socket, threading,time,os
# first, create a socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# then bind the local computer and assign the port
# bind
s.bind(('127.0.0.1',9999))

# limit the max number of the connection,there we limit 5
s.listen(5)
print 'Waiting for connection...',os.getpid()

# there is the handle for the new thread
def tcplink(sock,addr):
    print 'Accept new connection from %s %s' %addr
    sock.send('Welcome')
    while True:
        data = sock.recv(1024)
        print '%s from %s'%(data,addr)
        time.sleep(1)
        if data == 'exit' or not data:
            break
        sock.send('Hello,%s'%data)
    sock.close()
    print 'Connection from %s %s closed'%addr
# through a loop for listening the connection of a client,and use #accept() waiting/return a connection of client
while True:
    # receive a new connection
    sock,addr = s.accept()
    # create a new thread for handing the connection of TCP
    t = threading.Thread(target=tcplink,args=(sock,addr))
    t.start()
