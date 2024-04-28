### VLAN (Virtual Local Area Network)

VLAN is a network technology that enables the partitioning of a physical network into multiple logical networks. It allows you to segment a single physical network into multiple virtual networks, each with its own broadcast domain. VLANs are typically used to improve network performance, security, and scalability by isolating traffic and controlling communication between devices.

#### How VLAN Works:

1. **Port-based VLAN**: In port-based VLAN, network switches are configured to assign ports to specific VLANs. Devices connected to ports assigned to the same VLAN can communicate with each other as if they were on the same physical network.

2. **Tagged VLAN**: In tagged VLAN, frames are tagged with VLAN identifiers (VLAN IDs) as they traverse the network. This allows VLAN-aware devices to differentiate between traffic from different VLANs on the same physical network infrastructure.

3. **VLAN Trunking**: Trunking is used to carry traffic from multiple VLANs over a single network link between switches. VLAN trunking protocols (e.g., IEEE 802.1Q) encapsulate frames with VLAN tags, enabling switches to identify and separate traffic for different VLANs.

#### Python Code Demonstration:

Below is a simple Python code demonstrating VLAN implementation using the `scapy` library, which allows packet manipulation.

```python
from scapy.all import Ether, IP, UDP, sendp

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
```

This Python script creates two VLAN-tagged Ethernet frames, each with a different VLAN ID, and sends them out on the network interface specified (`eth0`). You can adjust the VLAN IDs, MAC addresses, and IP addresses according to your network setup.

Remember to install the `scapy` library (`pip install scapy`) before running the script.
