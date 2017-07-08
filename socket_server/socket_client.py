import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1",3000))
s.send("My name is Himanshu".encode())
data = s.recv(1000)
print("Recieved from server",data)
s.close()

print("Client is disconnected")