import socket

# Define host and port for the server
HOST = '127.0.0.1'  # localhost
PORT = 12345

# Create a UDP socket
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
    # Bind the socket to the host and port
    server_socket.bind((HOST, PORT))
    
    print("Server is listening for incoming messages...")
    
    # Receive and echo back messages
    while True:
        data, address = server_socket.recvfrom(1024)
        print("Received from", address, ":", data.decode())
        
        # Echo back the received message
        server_socket.sendto(data, address)
