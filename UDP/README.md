## Implementing UDP Communication in Python

### Objective:
To understand and implement basic UDP client-server communication using Python.

### Prerequisites:
- Basic knowledge of Python programming language.
- Understanding of networking concepts, particularly UDP protocol.

### Tools Required:
- Python interpreter (version 3.x recommended).

### Implementation Steps:

#### Step 1: Setting Up the Environment
1. Ensure Python is installed on your system. If not, download and install it from [Python's official website](https://www.python.org/downloads/).
2. Open a text editor or an Integrated Development Environment (IDE) to write Python code.

#### Step 2: Writing the UDP Server Program
1. Create a new Python script named `udp_server.py`.
2. Implement a UDP server that listens for incoming messages and echoes them back to the client.

```python
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
```

#### Step 3: Writing the UDP Client Program
1. Create a new Python script named `udp_client.py`.
2. Implement a UDP client that sends messages to the server and receives responses.

```python
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
```

#### Step 4: Running the Programs
1. Open two terminal windows or command prompts.
2. In one window, run the server program:
   ```
   $ python udp_server.py
   ```
3. In the other window, run the client program:
   ```
   $ python udp_client.py
   ```

### Conclusion:
We have successfully implemented basic UDP client-server communication using Python.