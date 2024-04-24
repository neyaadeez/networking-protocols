import socket

# Define host and port for the server
HOST = '127.0.0.1'  # localhost
PORT = 12345

# Create a UDP socket
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
    # Send messages to the server
    message = input("Enter message to send: ")
    client_socket.sendto(message.encode(), (HOST, PORT))
    
    # Receive response from the server
    response, address = client_socket.recvfrom(1024)
    print("Server response:", response.decode())
