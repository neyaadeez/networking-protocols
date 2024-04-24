import socket

# Define host and port for the server
HOST = '127.0.0.1'  # localhost
PORT = 12345

# Create a TCP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    # Connect to the server
    client_socket.connect((HOST, PORT))
    
    # Send data to the server
    message = input("Enter message to send: ")
    client_socket.sendall(message.encode())
    
    # Receive response from the server
    response = client_socket.recv(1024)
    print("Server response:", response.decode())