import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #TCP CONNECTION
s.connect(("192.168.100.5",8989))
msg = s.recv(1024)
print(msg.decode('ascii'))
s.close()