import socket

s = socket.socket()
print("socket is created")

port = 1976

s.bind(('',port))
print ("Socket is binded to %s" %(port))
s.listen(5)
print("Socket is listening")
while True:
	c, addr = s.accept()
	print("Got Connection From" , addr)