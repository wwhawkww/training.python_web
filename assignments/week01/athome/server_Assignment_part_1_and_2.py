
import socket
import sys


server = socket.socket(socket.AF_INET,socket.SOCK_STREAM,socket.IPPROTO_IP)
server_address = ('localhost', 50001)
server.bind(server_address)
server.listen(2)

while True:
	con, cli = server.accept()

	try:
		bob = con.recv(10)
		numbers = bob.split(",")
		output = 'Your entered sum: '+ str(int(numbers[0]) + int(numbers[1]))
		#input = 'Your send string is: ' + str(int(numbers[0]), int(numbers[1]))
		#con.sendall(input)
		con.sendall(output)
	except KeyboardInterrupt:
		server.close()
	finally:
		con.close()
server.close()