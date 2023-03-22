import socket

# Replace the forwarding URL with your own
ngrok_url = "http://1234abcd.ngrok.io"

# create a socket object
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
clientsocket.connect(('localhost', 80))

# receive data from the server
data = clientsocket.recv(1024)

print(f"Received message: {data.decode()}")

# close the socket
clientsocket.close()
