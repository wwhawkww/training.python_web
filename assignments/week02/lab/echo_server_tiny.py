
import socket
import sys


server = socket.socket(socket.AF_INET,socket.SOCK_STREAM,socket.IPPROTO_IP)
server_address = ('localhost', 50000)
server.bind(server_address)
server.listen(2)

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

		#numbers = bob.split(",")
		#output = 'Your entered sum: '+ str(int(numbers[0]) + int(numbers[1]))
		#input = 'Your send string is: ' + str(int(numbers[0]), int(numbers[1]))
		#con.sendall(input)
		con.sendall(text)
	except KeyboardInterrupt:
		server.close()
	finally:
		con.close()
server.close()