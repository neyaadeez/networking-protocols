from scapy.all import Ether, IP, UDP, BOOTP, DHCP, sendp, sniff

def dhcp_discover():
    # Build DHCP discover packet
    dhcp_discover = Ether(dst="ff:ff:ff:ff:ff:ff") / \
                    IP(src="0.0.0.0", dst="255.255.255.255") / \
                    UDP(sport=68, dport=67) / \
                    BOOTP(chaddr="Your_MAC_Address_Here") / \
                    DHCP(options=[("message-type", "discover"), "end"])
    
    # Send DHCP discover packet
    sendp(dhcp_discover)

def handle_dhcp_offer(packet):
    if DHCP in packet and packet[DHCP].options[0][1] == 2:  # DHCP Offer
        print("DHCP Offer Received:")
        print(packet.summary())

# Sniff DHCP Offer responses
sniff(prn=handle_dhcp_offer, filter="udp and (port 67 or port 68)", store=0, timeout=10)

# Send DHCP Discover
dhcp_discover()
