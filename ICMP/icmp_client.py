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
