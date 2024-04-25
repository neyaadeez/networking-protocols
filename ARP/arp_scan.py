from scapy.all import ARP, Ether, srp

def arp_scan(ip):
    # Create ARP packet
    arp_request = ARP(pdst=ip)
    # Create Ethernet frame
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    # Combine Ethernet frame and ARP packet
    packet = ether / arp_request
    # Send packet and capture responses
    result = srp(packet, timeout=3, verbose=False)[0]
    
    # Extract MAC addresses from responses
    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})
    
    return devices

# Example usage
if __name__ == "__main__":
    ip_range = "192.168.1.1/24"
    devices = arp_scan(ip_range)
    print("IP Address\tMAC Address")
    print("--------------------------")
    for device in devices:
        print(f"{device['ip']}\t{device['mac']}")
