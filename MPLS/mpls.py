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
packet = {'source_ip': '10.0.0.1', 'destination_ip': '10.0.0.2'}
print(f"Sending packet from {packet['source_ip']} to {packet['destination_ip']}\n")

# Packet forwarding through MPLS routers
packet_info = router_A.forward_packet(packet)
if packet_info:
    packet_info = router_B.forward_packet(packet_info['packet'])
if packet_info:
    packet_info = router_C.forward_packet(packet_info['packet'])
if packet_info:
    print(f"\nPacket reached its destination {packet_info['next_hop']} with label {packet_info['label']}")
