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
