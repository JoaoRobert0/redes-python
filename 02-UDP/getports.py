import socket

port_number = socket.getservbyname('domain')
print(port_number)

service_name = socket.getservbyport(port_number)
print(service_name)