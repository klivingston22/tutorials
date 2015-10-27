import socket 

hostname = raw_input ("Insert IP address: ")


hostIP = socket.getfqdn(hostname)

print hostIP 
print hostIP

