# Client
import socket
import ssl

# Server settings
HOST = 'localhost'
PORT = 12345

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Wrap the socket with SSL
ssl_context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
client_socket_ssl = ssl_context.wrap_socket(client_socket, server_hostname=HOST)

# Connect to the server
client_socket_ssl.connect((HOST, PORT))

# Send data to the server
message = "Hello from the client!"
client_socket_ssl.send(message.encode())

# Receive a response from the server
response = client_socket_ssl.recv(1024)
print("Response from server:", response.decode())

# Close the connection
client_socket_ssl.close()
