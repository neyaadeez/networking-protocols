import socket

# Define host and port for the server
HOST = '127.0.0.1'  # localhost
PORT = 12345

# Create a TCP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    # Bind the socket to the host and port
    server_socket.bind((HOST, PORT))
    
    # Start listening for incoming connections
    server_socket.listen()
    print("Server is listening for incoming connections...")
    
    # Accept incoming connections
    connection, address = server_socket.accept()
    print("Connected to:", address)
    
    with connection:
        # Receive data from the client
        while True:
            data = connection.recv(1024)
            if not data:
                break
            print("Received:", data.decode())
            
            # Echo back the received data
            connection.sendall(data)