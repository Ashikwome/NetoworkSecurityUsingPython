#buldiing a webserver using python

import socket

HOST , PORT = '',7777

listen_socket =  socket.socket(socket.AF_INET,socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
listen_socket.bind((HOST , PORT))
listen_socket.listen(1)

print ('Socket is serving %s' %PORT)

while True:
	client_connection , client_address = listen_socket.accept()
	request = client_connection(1234)
	print(request.decode('utf-8'))

	http_response = """\

	HTTP/1.1 200 ok

	hello world

	"""

	client_connection.sendall(bytes(http_response))
	client_connection.close()
