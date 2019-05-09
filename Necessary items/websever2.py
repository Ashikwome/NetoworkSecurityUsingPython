import socket

s = socket.socket()
print "Socket is Sucessfully created"

port = 1234

s.bind(("",port))
print "Socket is binded to %s" %(port)

s.listen(5)
print "socket is listening"

while True:
	c, addr = s.accept()
	print "Got Connection From" , addr
