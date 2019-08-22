import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = '127.0.0.1'
tcp_port = 5000
result = sock.connect_ex((address, tcp_port))
if result == 0:
   print("Port {} on {} is open".format(tcp_port, address))
else:
   print("Port {} on {} is closed".format(tcp_port, address))
sock.close()