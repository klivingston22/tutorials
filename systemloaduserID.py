import socket
import datetime
import os

HOST, PORT = '', 8888

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print 'Serving HTTP on port %s ... ' % PORT

while True:
	client_connection, client_address = listen_socket.accept()
	request = client_connection.recv(1024)
	print request
	http_response = """\
HTTP/1.1 200 OK

Hello, World!
The time is """ + str(datetime.datetime.now()) + """
System load is -  """ + str(os.getloadavg()) + """
Current Environment: """ + str(os.environ["HOME"]) + """
Current User ID: """ + (os.getlogin())

	client_connection.sendall(http_response)
	client_connection.close()
