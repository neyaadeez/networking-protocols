### MPLS (Multiprotocol Label Switching)

**Introduction:**
Multiprotocol Label Switching (MPLS) is a protocol-agnostic routing technique designed to speed up and shape traffic flows across networks. It operates between Layer 2 (Data Link Layer) and Layer 3 (Network Layer) of the OSI model. MPLS works by adding a label (or tag) to data packets, which is used to determine the forwarding path through the network. This label replaces traditional routing methods based solely on IP addresses, allowing for more efficient and flexible routing decisions.

**How MPLS Works:**
1. **Label Distribution Protocol (LDP)**: MPLS routers use LDP to exchange label information and build a Label Switched Path (LSP) across the network.
2. **Label Pushing**: When a packet enters the MPLS network, the ingress router assigns a label to it based on predefined forwarding rules.
3. **Label Switching**: Each router along the path examines the label and forwards the packet based on the label rather than the IP header.
4. **Label Popping**: When the packet reaches its destination, the egress router removes the MPLS label before delivering it to the final destination based on the IP header.

**Python Code to Simulate MPLS Routing:**

```python
class MPLSRouter:
    def __init__(self, name):
        self.name = name
        self.routing_table = {}

    def add_route(self, prefix, label, next_hop):
        self.routing_table[prefix] = {'label': label, 'next_hop': next_hop}

    def forward_packet(self, packet):
        destination_ip = packet['destination_ip']
        if destination_ip in self.routing_table:
            label = self.routing_table[destination_ip]['label']
            next_hop = self.routing_table[destination_ip]['next_hop']
            print(f"{self.name}: Forwarding packet to {next_hop} with label {label}")
            return {'packet': packet, 'label': label, 'next_hop': next_hop}
        else:
            print(f"{self.name}: No route found for destination {destination_ip}")

# Create MPLS routers
router_A = MPLSRouter('Router A')
router_B = MPLSRouter('Router B')
router_C = MPLSRouter('Router C')

# Add routes to routing tables
router_A.add_route('10.0.0.2', 100, 'Router B')
router_B.add_route('10.0.0.3', 200, 'Router C')
router_C.add_route('10.0.0.4', 300, 'Router D')

# Simulate packet forwarding
packet = {'source_ip': '10.0.0.1', 'destination_ip': '10.0.0.4'}
print(f"Sending packet from {packet['source_ip']} to {packet['destination_ip']}\n")

# Packet forwarding through MPLS routers
packet_info = router_A.forward_packet(packet)
if packet_info:
    packet_info = router_B.forward_packet(packet_info['packet'])
if packet_info:
    packet_info = router_C.forward_packet(packet_info['packet'])
if packet_info:
    print(f"\nPacket reached its destination {packet_info['next_hop']} with label {packet_info['label']}")
```

This Python code simulates a simple MPLS network with three routers (Router A, Router B, and Router C). Each router has a routing table that maps destination IP addresses to MPLS labels and next-hop routers. The code demonstrates how a packet is forwarded through the network using MPLS label switching.