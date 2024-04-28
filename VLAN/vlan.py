from scapy.all import Ether, IP, UDP, sendp, Dot1Q

# Define VLAN IDs
vlan_id1 = 10
vlan_id2 = 20

# Define source and destination MAC addresses
src_mac = "00:00:00:00:00:01"  # Source MAC address
dst_mac = "00:00:00:00:00:02"  # Destination MAC address

# Define source and destination IP addresses
src_ip = "192.168.1.1"  # Source IP address
dst_ip = "192.168.1.2"  # Destination IP address

# Create VLAN-tagged Ethernet frames
vlan_frame1 = Ether(src=src_mac, dst=dst_mac) / Dot1Q(vlan=vlan_id1) / IP(src=src_ip, dst=dst_ip)
vlan_frame2 = Ether(src=src_mac, dst=dst_mac) / Dot1Q(vlan=vlan_id2) / IP(src=src_ip, dst=dst_ip)

# Send VLAN-tagged frames
sendp(vlan_frame1, iface="eth0")
sendp(vlan_frame2, iface="eth0")
