import socket

# Replace the forwarding URL with your own
ngrok_url = "https://8cf4-2600-3c04-00-f03c-93ff-fe4d-14b6.ngrok.io"

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to a public host and a well-known port
serversocket.bind(('0.0.0.0', 80))

# start listening for incoming connections
serversocket.listen(1)

print("Waiting for incoming connections...")

# accept a connection
(clientsocket, address) = serversocket.accept()

print(f"Received connection from {address}")

# send "Hello, World!" to the client
clientsocket.send("Hello, World!".encode())

# close the socket
clientsocket.close()
serversocket.close()
