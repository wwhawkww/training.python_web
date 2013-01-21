
import socket
import sys

# Create a TCP/IP socket
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM,socket.IPPROTO_IP)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 50001)
client.connect(server_address)

try:
    # Send data
    	# Send numbers as string in format '#,#'
	# Send numbers to server  as string in format '#,#'
	sent_numbers = '5,600'
	client.sendall(sent_numbers)

    # print the response
	reciever = client.recv(25)
	print str(reciever)
	
finally:
    # close the socket to clean up
	client.close()
