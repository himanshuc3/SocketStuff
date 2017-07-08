import socket 
import sys

def get_host_info(host_name = ""):
	if host_name == "":
		host_name = socket.gethostname()
	try:	
		ip_address = socket.gethostbyname(host_name)
		print("Host Name : %s" % host_name)
		print("IP Addess : %s " % ip_address)
	except (socket.gaierror, e):
		print ("Couldn't connect to te host name: %s -- Error %s") % (host_name, e)	
	except (socket.error, e):
		print (" Connection error: %s" )% e

if(len(sys.argv) == 1):
	get_host_info()	
else:	
	get_host_info(sys.argv[1])