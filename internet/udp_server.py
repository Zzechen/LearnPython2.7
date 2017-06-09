# UDP is a protocol for no connection
# you can't need to create a connection,and you only know the IP and port of the aim,you can send data but
# don't know whether the msg is received
import socket
# now use a socket obj bind the server,there is a different with TCP at second param
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('127.0.0.1',9999))

# listen all the client,but unlike TCP that need to call 'listen()'
print 'Bind UDP on 9999'
while True:
    #receive data
    data,addr = s.recvfrom(1024)
    print 'Received from %s:%s' % addr
    s.sendto('Hello,%s!' % data,addr)

