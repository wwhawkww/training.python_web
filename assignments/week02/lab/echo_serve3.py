
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

def ok_response(GET,CODE):
	responder = "HTTP/1.1 200 OK"
	header = "Content-Type: text/html"
	empty = ""
	output = "Your GET command was: " + GET
	body = tinny_reader()
	response = "\r\n".join([responder, header, empty, body + output])
	return response

def parse_request():
	x=1

while True:
	con, cli = server.accept()

	try:
		bob = con.recv(1000)
		
		responder= bob.strip("\n").split("\r")
		
		for i in range(len(responder)):
			if "GET" in responder[i]:
				print "GET Confirmed"
				Confirmation1 = True
				GET = i
		
			if "Accept" and "text/html" in responder[i]:
				print "Code 200 Confirmed"
				Confirmation2 = True
				Code_200 = i
					
		if Confirmation1 and Confirmation2 != True:
			con.sendall("400 Bad Request")
			con.close()
		
		output = ok_response(responder[GET], responder[Code_200])
		con.sendall(output)
		
	except KeyboardInterrupt:
		server.close()
	
	finally:
		con.close()
server.close()