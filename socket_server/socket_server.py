import socket



# AF_INET = IPv4 tech used
#SOCK_STREAM = bidirectional dat flow between client and server
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(("127.0.0.1",3000)) # bind to my local machine
print("listening for connections..........")
s.listen(1) # number of maximum connections possible(client to server)

connection,address = s.accept()
print("Connected to client", address)

while 1:
	data = connection.recv(1000) #1000 =  number of bytes in one package -- should be nor way less neither way more
	if not data: break
	print("Recieved from client:", data.decode())
	connection.send(data.encode())


connection.close()	

