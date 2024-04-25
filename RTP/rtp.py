import socket
import struct
import time

# RTP header fields
VERSION = 2
PADDING = 0
EXTENSION = 0
CC = 0
MARKER = 0
PT = 0  # Payload Type

# Randomly chosen sequence number and timestamp for demonstration
SEQ_NUM = 1234
TIMESTAMP = int(time.time())

# Destination IP and port
DEST_IP = '127.0.0.1'
DEST_PORT = 12345

# Payload data (dummy data for demonstration)
payload_data = b'Hello, RTP!'

# Create RTP packet
rtp_packet = struct.pack('!BBHII', (VERSION << 6) | (PADDING << 5) | (EXTENSION << 4) | CC,
                         (MARKER << 7) | PT, SEQ_NUM, TIMESTAMP, 0) + payload_data

# Create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send RTP packet
sock.sendto(rtp_packet, (DEST_IP, DEST_PORT))

# Close socket
sock.close()