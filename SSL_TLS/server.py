# Server
import socket
import ssl

# Server settings
HOST = 'localhost'
PORT = 12345
CERTFILE = 'server.crt'  # Server's SSL certificate
KEYFILE = 'server.key'   # Server's private key

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Wrap the socket with SSL
ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
ssl_context.load_cert_chain(certfile=CERTFILE, keyfile=KEYFILE)
server_socket_ssl = ssl_context.wrap_socket(server_socket, server_side=True)

# Bind and listen
server_socket_ssl.bind((HOST, PORT))
server_socket_ssl.listen()

print("Server is listening...")

# Accept incoming connections
while True:
    client_socket_ssl, client_address = server_socket_ssl.accept()
    print("Connected to:", client_address)

    # Receive data from the client
    data = client_socket_ssl.recv(1024)
    print("Received:", data.decode())

    # Send a response back to the client
    response = "Hello from the server!"
    client_socket_ssl.send(response.encode())

    # Close the connection
    client_socket_ssl.close()
