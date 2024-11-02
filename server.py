import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #TCP CONNECTION
s.bind(("192.168.100.5",8989))
s.listen(1)
print("Run server...\n")
c , addr = s.accept()
print("connect to %s" % str(addr))
msg = "hello" 
c.sendall(msg.encode('ascii'))
c.close()
