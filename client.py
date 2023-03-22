import socket

# Replace the forwarding URL with your own
ngrok_url = "https://8cf4-2600-3c04-00-f03c-93ff-fe4d-14b6.ngrok.io"

# create a socket object
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
clientsocket.connect(('localhost', 80))

# receive data from the server
data = clientsocket.recv(1024)

print(f"Received message: {data.decode()}")

# close the socket
clientsocket.close()
