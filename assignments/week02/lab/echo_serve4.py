
# import modules
import socket, sys, os

#server settings and binding
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM,socket.IPPROTO_IP)
server_address = ('localhost', 50000)
server.bind(server_address)
server.listen(1)

# filepath creation
path_NAME= os.path.realpath(__file__)
source_path = "/".join(path_NAME.split("/")[:-1])+"/"


def tinny_reader():
	location = source_path + "tiny.html"
	opener = open(location)
	texter = opener.read()
	return str(texter)

def HTTP_reader(PATH):
	opener = open(PATH)
	texter = opener.read()
	return str(texter)

def resolve_uri(GET):
	import os
	ERROR = "200 OK"
	try:
		dirList=os.listdir(source_path)
		pathname = GET.split(" ")[1].split("/")[1]
		print "Pathname: " + pathname
	except(OSError):
		print "OSError: " + pathname + "not found"
		ERROR = 204
	if len(GET.split(" ")[1].split("/")) > 2:
		pathname_x = GET.split(" ")[1].split("/")[2]
		try:
			dirList_x = os.listdir(source_path+"/"+pathname+"/")
			if pathname_x in dirList_x:
				print "found the file!"
				ERROR = "200 OK"
			else:
				print "ERROR: file not found"
				ERROR = "206 PARTIAL CONTENT"
				
		except(OSError):
			print "OSError: " + pathname_x + "not found"
			ERROR = "204 NO CONTENT"
	
	if pathname in dirList and "200" in ERROR:
		return True, ERROR
	else:
		print "ERROR: directory not found"
		ERROR = "204 NO CONTENT"
		return False, ERROR
	
		

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
				
			if "HOST" in responder[i].upper():
				print responder[i].split(": ")[1]
					
		if Confirmation1 and Confirmation2 != True:
			con.sendall("400 Bad Request")
			con.close()
		
		feedback, ERROR = resolve_uri(responder[GET])
		
		if feedback == True:
			print "uri resolved: " + responder[GET]
			print "HTTP/1.1 - " + str(ERROR)
			print responder[GET].split(" ")[1]
			output = HTTP_reader(source_path[:-1] + str(responder[GET].split(" ")[1] ))
			con.sendall(output)
			print "feedback True loop"
		
		else:	
			output = ok_response(responder[GET], responder[Code_200]) +'<br>' + "HTTP/1.1 file response: " + "<b>"+str(ERROR)
			con.sendall(output)
			print "feedback false loop"
		
	except KeyboardInterrupt:
		server.close()
	
	finally:
		con.close()
server.close()