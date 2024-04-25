# ICMP Communication Protocol Demonstration

## Introduction
ICMP (Internet Control Message Protocol) is a network layer protocol used to send error messages and operational information, such as network status or debugging information. It is commonly used for diagnostic and control purposes in IP networks.

This README provides an explanation of how ICMP works and demonstrates a simple ICMP client-server communication using Python.

## How ICMP Works
ICMP operates by sending control messages between devices on an IP network. These messages are encapsulated within IP packets and are used for various purposes, including:

- Reporting errors (e.g., unreachable destination, time exceeded)
- Network status monitoring (e.g., ping requests and responses)
- Path MTU (Maximum Transmission Unit) discovery
- Redirecting packets to a better route

ICMP messages typically include an ICMP header and, optionally, an IP header and data payload. The ICMP header contains fields such as message type, code, and checksum.

## Implementation: ICMP Client-Server Communication in Python

### Server Program (`icmp_server.py`)

```python
import os
import socket
import struct
import sys

# Create a raw socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)

# Receive and print ICMP packets
while True:
    packet, address = server_socket.recvfrom(1024)
    ip_header = packet[:20]
    iph = struct.unpack('!BBHHHBBH4s4s', ip_header)
    version_ihl = iph[0]
    ihl = version_ihl & 0xF
    iph_length = ihl * 4
    src_ip = socket.inet_ntoa(iph[8])
    print("Received ICMP packet from:", src_ip)
    icmp_header = packet[iph_length:iph_length + 8]
    icmph = struct.unpack('!BBHHH', icmp_header)
    icmp_type = icmph[0]
    code = icmph[1]
    print("ICMP Type:", icmp_type)
    print("Code:", code)
    print("Data:", packet[iph_length + 8:])
```

### Client Program (`icmp_client.py`)

```python
import os
import socket
import struct
import sys

# Function to calculate checksum
def calculate_checksum(data):
    s = 0
    for i in range(0, len(data), 2):
        w = (data[i] << 8) + (data[i+1])
        s = s + w

    s = (s >> 16) + (s & 0xffff)
    s = ~s & 0xffff
    return s

# Create a raw socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
client_socket.setsockopt(socket.SOL_IP, socket.IP_TTL, struct.pack('I', 64))  # Set TTL to 64

# Define destination IP address
dest_ip = "127.0.0.1"

# Craft ICMP echo request packet
icmp_type = 8  # ICMP echo request
code = 0
checksum = 0
identifier = os.getpid() & 0xFFFF
seq_number = 1
icmp_header = struct.pack('!BBHHH', icmp_type, code, checksum, identifier, seq_number)

# Calculate checksum
checksum = calculate_checksum(icmp_header)
icmp_header = struct.pack('!BBHHH', icmp_type, code, checksum, identifier, seq_number)

# Send ICMP echo request packet
client_socket.sendto(icmp_header, (dest_ip, 0))

# Receive ICMP echo reply packet
packet, address = client_socket.recvfrom(1024)
print("Received ICMP echo reply from:", address[0])
```

### Running the Programs
1. Open two terminal windows or command prompts.
2. In one window, run the server program:
   ```
   $ python icmp_server.py
   ```
3. In the other window, run the client program:
   ```
   $ python icmp_client.py
   ```

### Simple ICMP ping using Python

```python
import socket
import struct
import select
import time

# Define the ICMP echo request type and code
ICMP_ECHO_REQUEST = 8
ICMP_CODE = socket.getprotobyname('icmp')

def checksum(data):
    """
    Calculate the checksum for the given data.
    """
    # If the length of data is odd, pad it with zero
    if len(data) % 2:
        data += b'\x00'

    # Initialize the checksum to zero
    checksum_value = 0

    # Iterate over the data, summing up 16-bit chunks
    for i in range(0, len(data), 2):
        checksum_value += (data[i] << 8) + (data[i + 1])

    # Fold any overflow back into the result
    checksum_value = (checksum_value & 0xffff) + (checksum_value >> 16)

    # Return the complement of the checksum
    return ~checksum_value & 0xffff

def send_icmp_request(destination_ip):
    # Create a raw socket
    icmp_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, ICMP_CODE)

    # Set the timeout for the socket
    icmp_socket.settimeout(1)

    # Create an ICMP header with type 8 (echo request) and code 0
    icmp_header = struct.pack('!BBHHH', ICMP_ECHO_REQUEST, 0, 0, 0, 1)

    # Generate a dummy payload
    payload = b'ping'

    # Calculate the checksum for the ICMP header and payload
    icmp_checksum = checksum(icmp_header + payload)

    # Replace the checksum in the header
    icmp_header = struct.pack('!BBHHH', ICMP_ECHO_REQUEST, 0, icmp_checksum, 0, 1)

    # Construct the packet by combining the ICMP header and payload
    packet = icmp_header + payload

    try:
        # Send the packet to the destination IP
        start_time = time.time()
        icmp_socket.sendto(packet, (destination_ip, 0))
        
        # Wait for a response or timeout
        ready, _, _ = select.select([icmp_socket], [], [], 1)
        end_time = time.time()

        if ready:
            # Receive the reply packet
            reply_packet, _ = icmp_socket.recvfrom(1024)
            round_trip_time = (end_time - start_time) * 1000
            print(f"Ping successful. Round trip time: {round_trip_time:.2f} ms")
        else:
            print("Ping failed. No reply received.")
    except socket.error as e:
        print(f"Ping failed: {e}")
    finally:
        # Close the socket
        icmp_socket.close()

if __name__ == "__main__":
    destination_ip = "8.8.8.8"
    send_icmp_request(destination_ip)
```

This Python script sends an ICMP echo request packet to the specified destination IP address (in this case, the Google DNS server 8.8.8.8) and waits for the echo reply. If a reply is received, it prints the round-trip time. Otherwise, it indicates that the ping failed. Please note that raw socket operations require root/administrator privileges on most operating systems.