#connection with google

import socket
import sys

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print "Socket is sucesfully created"
except socket.error as err:
	print "failed"

port = 80

try:
	host_ip = socket.gethostbyname("www.google.com")
except socket.gaierror:
	print ("There was an error resolving the host")
	sys.exit()

s.connect((host_ip,port))

print ("sucesfully connected \ on port == %s" %(host_ip))