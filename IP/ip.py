from scapy.all import IP, ICMP, send

# Define the destination IP address
destination_ip = "8.8.8.8"

# Craft an IP packet with ICMP (ping) payload
packet = IP(dst=destination_ip) / ICMP()

# Send the packet
send(packet)

print("Packet sent successfully.")