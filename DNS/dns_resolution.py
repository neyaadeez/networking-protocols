import socket

def resolve_domain(domain_name):
    try:
        ip_address = socket.gethostbyname(domain_name)
        print(f"The IP address of {domain_name} is: {ip_address}")
    except socket.gaierror:
        print(f"Unable to resolve the IP address of {domain_name}")

# Replace 'example.com' with the domain name you want to resolve
domain_to_resolve = 'example.com'
resolve_domain(domain_to_resolve)