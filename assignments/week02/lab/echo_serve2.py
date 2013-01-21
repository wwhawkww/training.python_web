
import socket
import sys


server = socket.socket(socket.AF_INET,socket.SOCK_STREAM,socket.IPPROTO_IP)
server_address = ('localhost', 50000)
server.bind(server_address)
server.listen(2)

def tinny_reader():
	location = "/Users/wwhawkww/Documents/Programming/UW Python Classes/Class 2 - Internet Programming in Python/training.python_web/assignments/week02/tiny.html"
	opener = open(location)
	texter = opener.read()
	return str(texter)

def ok_response():
	responder = "HTTP/1.1 200 OK"
	header = "Content-Type: text/html"
	empty = ""
	body = tinny_reader()
	response = "\r\n".join([responder, header, empty, body])
	return response

while True:
	con, cli = server.accept()

	try:
		bob = con.recv(1000)
		
		text = """
		<html>
		<body>
		<h1>This is a header</h1>
		<p>
		and this is some regular text
		</p>
		<p>
		and some more
		</p>
		</body>
		</html>
		"""
		output = ok_response()
		print output, "OK"
		#numbers = bob.split(",")
		#output = 'Your entered sum: '+ str(int(numbers[0]) + int(numbers[1]))
		#input = 'Your send string is: ' + str(int(numbers[0]), int(numbers[1]))
		#con.sendall(input)
		con.sendall(output)
	except KeyboardInterrupt:
		server.close()
	finally:
		con.close()
server.close()