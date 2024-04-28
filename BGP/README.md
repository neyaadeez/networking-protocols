### BGP (Border Gateway Protocol)

BGP (Border Gateway Protocol) is a standardized exterior gateway protocol designed to exchange routing information between different autonomous systems (ASes) on the Internet. It is the protocol used to make core routing decisions on the Internet.

#### How BGP Works:
1. **Neighbor Establishment**: BGP routers establish TCP connections with each other to form peer relationships. These connections are typically established over port 179.

2. **Route Advertisement**: Once the peer relationships are established, BGP routers exchange routing information, known as network layer reachability information (NLRI), along with various attributes describing the paths to reach those networks.

3. **Path Selection**: BGP routers use various attributes (e.g., AS path length, origin type, local preference) to select the best paths to reach each network. The best path is then stored in the routing table.

4. **Route Propagation**: BGP routers propagate the selected routes to their neighbors, which in turn propagate them further, ensuring that routing information is distributed throughout the Internet.

5. **Route Maintenance**: BGP routers continuously monitor the reachability of routes and update their routing tables accordingly. If a path becomes unavailable or a better path is discovered, BGP routers adjust their routing tables and propagate the changes to their neighbors.

### Python Implementation of BGP

Below is a simple Python implementation of a basic BGP router using the `socket` library for TCP communication:

```python
import socket
import struct

# BGP message types
OPEN = 1
UPDATE = 2
NOTIFICATION = 3
KEEPALIVE = 4

# BGP OPEN message parameters
MY_AS = 65001
MY_BGP_ID = "10.25.90.1"
HOLD_TIME = 180
BGP_VERSION = 4

def create_open_message():
    marker = b'\xff' * 16
    header = struct.pack("!16sHB", marker, 29, OPEN)
    body = struct.pack("!HHBBBB", BGP_VERSION, MY_AS, HOLD_TIME, len(MY_BGP_ID.split('.')), *[int(octet) for octet in MY_BGP_ID.split('.')])
    return header + body

def send_bgp_open(peer_ip, peer_port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((peer_ip, peer_port))
    open_message = create_open_message()
    sock.send(open_message)
    print("Sent BGP OPEN message to {}:{}".format(peer_ip, peer_port))
    sock.close()

def main():
    peer_ip = "10.25.0.1"  # Peer IP address
    peer_port = 179  # BGP default port
    send_bgp_open(peer_ip, peer_port)

if __name__ == "__main__":
    main()
```

This code demonstrates sending a BGP OPEN message to a peer IP address and BGP port. It creates the OPEN message packet according to the BGP protocol specification and sends it using a TCP socket. Note that this code only demonstrates the OPEN message and does not handle other BGP message types or maintain a full BGP session.