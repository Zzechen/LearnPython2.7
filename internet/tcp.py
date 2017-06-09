import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('www.sina.com.cn',80))
#send data
s.send('GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

#receive data
buffer = []
while True:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = ''.join(buffer)
# close
s.close()

# let us write the data into a file
#first we should remove the header of the http
header,html=data.split('\r\n\r\n',1)
print header

# write into a file
with open('sina.html','wb') as f:
    f.write(html)
