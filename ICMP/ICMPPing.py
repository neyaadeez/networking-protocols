import socket
import struct
import select
import time

# Define the ICMP echo request type and code
ICMP_ECHO_REQUEST = 8
ICMP_CODE = socket.getprotobyname('icmp')

def checksum(data):
    """
    Calculate the checksum for the given data.
    """
    # If the length of data is odd, pad it with zero
    if len(data) % 2:
        data += b'\x00'

    # Initialize the checksum to zero
    checksum_value = 0

    # Iterate over the data, summing up 16-bit chunks
    for i in range(0, len(data), 2):
        checksum_value += (data[i] << 8) + (data[i + 1])

    # Fold any overflow back into the result
    checksum_value = (checksum_value & 0xffff) + (checksum_value >> 16)

    # Return the complement of the checksum
    return ~checksum_value & 0xffff

def send_icmp_request(destination_ip):
    # Create a raw socket
    icmp_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, ICMP_CODE)

    # Set the timeout for the socket
    icmp_socket.settimeout(1)

    # Create an ICMP header with type 8 (echo request) and code 0
    icmp_header = struct.pack('!BBHHH', ICMP_ECHO_REQUEST, 0, 0, 0, 1)

    # Generate a dummy payload
    payload = b'ping'

    # Calculate the checksum for the ICMP header and payload
    icmp_checksum = checksum(icmp_header + payload)

    # Replace the checksum in the header
    icmp_header = struct.pack('!BBHHH', ICMP_ECHO_REQUEST, 0, icmp_checksum, 0, 1)

    # Construct the packet by combining the ICMP header and payload
    packet = icmp_header + payload

    try:
        # Send the packet to the destination IP
        start_time = time.time()
        icmp_socket.sendto(packet, (destination_ip, 0))
        
        # Wait for a response or timeout
        ready, _, _ = select.select([icmp_socket], [], [], 1)
        end_time = time.time()

        if ready:
            # Receive the reply packet
            reply_packet, _ = icmp_socket.recvfrom(1024)
            round_trip_time = (end_time - start_time) * 1000
            print(f"Ping successful. Round trip time: {round_trip_time:.2f} ms")
        else:
            print("Ping failed. No reply received.")
    except socket.error as e:
        print(f"Ping failed: {e}")
    finally:
        # Close the socket
        icmp_socket.close()

if __name__ == "__main__":
    destination_ip = "8.8.8.8"
    send_icmp_request(destination_ip)
