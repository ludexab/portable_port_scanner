#!/bin/python3

import sys
import socket
from datetime import datetime

# Checking argument input
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) # Defining our target IP address
else:
	print("Invalid IP address \n Syntax: python3 scanner.py <ip>")
	
# BANNER
print("-" * 50)
print("Starting port scan of target {}".format(target))
print("Time Started: {}".format(datetime.now()))
print("-" * 50)

# Loop through port numbers against the IP address to check if it is open
# We'll run the loop in a try block for better error handling
try:
	progress = 0
	for port in range(50,85):
		progress += 2.941
		progress = int(progress)		
		soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 			# Create a socket object
		socket.setdefaulttimeout(1) 							# Set timeout of 1 sec
		result = soc.connect_ex((target,port))						# Create a connection to the port
		if result == 0:
			print(f"port {port} is open")						# Print using string formatting
		soc.close()									# Close the connection to the port
		print("{}% completed".format(str(progress)), end="\r", flush=True)		# Show scan progress
except KeyboardInterrupt:
	print("Exiting the scan")
	sys.exit()
except socket.gaierror:
	print("Hostname could not be resolved")
	sys.exit()
except socket.error:
	print("Could not connect to server")
	sys.exit()
