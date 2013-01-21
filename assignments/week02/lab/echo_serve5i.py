
# import modules
import socket, sys, os

path_NAM= os.path.realpath(__file__)
MOD_PATH = "/".join(path_NAM.split("/")[:-1])+"/web/"
sys.path.append(MOD_PATH)
#sys.path.append('/Users/wwhawkww/Documents/Programming/UW Python Classes/Class 2 - Internet Programming in Python/training.python_web/assignments/week02/lab/web/')
import make_time

#server settings and binding
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM,socket.IPPROTO_IP)
server_address = ('localhost', 50000)
server.bind(server_address)
server.listen(1)

# filepath creation
path_NAME= os.path.realpath(__file__)
source_path = "/".join(path_NAME.split("/")[:-1])+"/"


def tinny_reader():
	location = source_path + "/web/a_web_page.html"
	opener = open(location)
	texter = opener.read()
	return str(texter)

def HTTP_reader(PATH,add_time):
	opener = open(PATH)
	texter = opener.read()
	if add_time == True:
		html_time = make_time.time_time()
		html_text = tinny_reader()
		return html_text+ '<br><br>' + str(html_time)
	else:
		return str(texter)

def resolve_uri(GET):
	import os
	ERROR = "200 OK"
	try:
		dirList=os.listdir(source_path)
		pathname = GET.split(" ")[1].split("/")[1]
	except(OSError):
		ERROR = 204
	if len(GET.split(" ")[1].split("/")) > 2:
		pathname_x = GET.split(" ")[1].split("/")[2]
		try:
			dirList_x = os.listdir(source_path+"/"+pathname+"/")
			if pathname_x in dirList_x:
				ERROR = "200 OK"
			else:
				ERROR = "206 PARTIAL CONTENT"
				
		except(OSError):
			ERROR = "204 NO CONTENT"
	
	if pathname in dirList and "200" in ERROR:
		print pathname_x
		if "make_time" in pathname_x:
			add_time = True
			return True, ERROR, add_time
		else: return True, ERROR, False
	else:
		ERROR = "204 NO CONTENT"
		return False, ERROR,False
	
		

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
				Confirmation1 = True
				GET = i
		
			if "Accept" and "text/html" in responder[i]:
				Confirmation2 = True
				Code_200 = i
					
		if Confirmation1 and Confirmation2 != True:
			con.sendall("400 Bad Request")
			con.close()
		
		feedback, ERROR,add_time = resolve_uri(responder[GET])
		
		if feedback == True:
			print "uri resolved: " + responder[GET]
			print "HTTP/1.1 - " + str(ERROR)
			output = HTTP_reader(source_path[:-1] + str(responder[GET].split(" ")[1] ),add_time)
			con.sendall(output)
		
		else:	
			output = ok_response(responder[GET], responder[Code_200]) +'<br>' + "HTTP/1.1 file response: " + "<b>"+str(ERROR)
			con.sendall(output)
		
	except KeyboardInterrupt:
		con.close()
		server.close()
		sys.exit()
	
	finally:
		con.close()
server.close()