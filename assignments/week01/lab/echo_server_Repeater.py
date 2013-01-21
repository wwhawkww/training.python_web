# Server
import socket
import sys

# Create a TCP/IP socket
server = socket.socket(2,1,0)

# Bind the socket to the port
server_address = ('localhost', 50000)
server.bind(server_address)

# Listen for incoming connections
server.listen(2)

while True:
    # Wait for a connection
	con, cli = server.accept()
	print con

	try:
        # Receive the data and send it back+
		bob = con.recv(42)
		print bob
		con.sendall('reply')

	finally:
		print 'Made it to finally'
        # Clean up the connection
		server.close()