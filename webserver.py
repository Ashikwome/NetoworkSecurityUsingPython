#socket is the endpoint of a .py directional communication channel
#and it may communicate between or with in process  processies on the same machine or processies on different machine
#here we are going to create a server and ping google with it

#importing the socket library

import socket

#CREATING A SOCKET OBJECT

s = socket.socket()
print "Socket Created Sucessfully"


 
 #reserve a port number telling python to reserve a port on the physical machine
port = 1457 
 
 #binding the port  bangla   tar laganor moto code er sathe phycal computer er sathe communication establish korlam
 
s.bind(('',port))
print "Socket is binded to %s" %(port)
 
 #put the socket into listening mode
 
s.listen(5)
print "Socket is listening"
 
 	#interrupt ourselfe ie_exception or an error occur
while True:
 	
 	#establishing connection with the client
 	c, addr = s.accept()
 	print 'Got connection from' , addr
 