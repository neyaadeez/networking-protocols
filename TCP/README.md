## Implementing TCP Communication in Python

### Objective:
To understand and implement basic TCP client-server communication using Python.

### Prerequisites:
- Basic knowledge of Python programming language.
- Understanding of networking concepts, particularly TCP/IP protocol suite.

### Tools Required:
- Python interpreter (version 3.x recommended).

### Implementation Steps:

#### Step 1: Setting Up the Environment
1. Ensure Python is installed on your system. If not, download and install it from [Python's official website](https://www.python.org/downloads/).
2. Open a text editor or an Integrated Development Environment (IDE) to write Python code.

#### Step 2: Writing the TCP Server Program
1. Create a new Python script named `tcp_server.py`.
2. Implement a TCP server that listens for incoming connections and echoes received messages back to the client.

```python
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
```

#### Step 3: Writing the TCP Client Program
1. Create a new Python script named `tcp_client.py`.
2. Implement a TCP client that establishes a connection to the server and sends messages.

```python
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
```

#### Step 4: Running the Programs
1. Open two terminal windows or command prompts.
2. In one window, run the server program:
   ```
   $ python tcp_server.py
   ```
3. In the other window, run the client program:
   ```
   $ python tcp_client.py
   ```

### Conclusion:
We successfully implemented a basic TCP client-server communication using Python.