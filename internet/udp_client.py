import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
for data in ['Michael','Tracy','Sarah']:
    # send data
    s.sendto(data,('127.0.0.1',9999))
    # receive data
    print s.recv(1024)