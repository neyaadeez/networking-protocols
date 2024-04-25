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