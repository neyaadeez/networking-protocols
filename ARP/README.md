### Address Resolution Protocol (ARP) Explanation:

ARP is used to map a known IP address to a MAC (Media Access Control) address in a local network. When a device wants to communicate with another device on the same network, it needs to know the MAC address of the destination device. ARP helps in this process by broadcasting a request message to all devices in the network, asking for the MAC address corresponding to a given IP address. The device with the corresponding IP address responds with its MAC address, and the requesting device stores this mapping in its ARP cache for future use.

### Python Implementation:

Here's a simple Python code to demonstrate ARP functionality using the `scapy` library:

```python
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
```

### Instructions:

1. Install the `scapy` library using pip: `pip install scapy`.
2. Save the above code into a Python file, e.g., `arp_scan.py`.
3. Run the script (`python arp_scan.py`).
4. It will scan the specified IP range and print out the IP addresses and corresponding MAC addresses of the devices found in the network.

This Python code demonstrates ARP functionality by sending ARP requests to the specified IP range and capturing the responses to identify the devices present in the local network along with their MAC addresses.