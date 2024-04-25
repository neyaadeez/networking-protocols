### How DNS (Domain Name System) Works:

The Domain Name System (DNS) is a hierarchical decentralized naming system for computers, services, or any resource connected to the Internet or a private network. It translates domain names, which are human-readable identifiers, into IP addresses, which are used by computers to communicate with each other.

Here's a simplified overview of how DNS works:

1. **DNS Resolution Request**: When a user enters a domain name (e.g., www.example.com) into a web browser, the browser needs to know the corresponding IP address to establish a connection. It sends a DNS resolution request to a DNS resolver.

2. **DNS Resolver Lookup**: The DNS resolver is typically provided by the user's Internet Service Provider (ISP) or configured in the network settings. If it doesn't have the requested domain name and corresponding IP address in its cache, it forwards the request to a DNS root server.

3. **Root Server Query**: The root server doesn't contain the IP address for the requested domain name directly. Instead, it refers the resolver to the appropriate Top-Level Domain (TLD) server based on the domain's top-level domain extension (e.g., .com, .org, .net).

4. **TLD Server Lookup**: The TLD server manages the top-level domain (e.g., .com) and directs the resolver to the authoritative name server for the second-level domain (e.g., example.com).

5. **Authoritative Name Server Query**: The authoritative name server stores the DNS records (such as A, AAAA, CNAME, MX records) for the domain. It responds to the resolver with the requested IP address.

6. **DNS Resolution Response**: The resolver receives the IP address from the authoritative name server and caches it for future use. It then returns the IP address to the user's browser, which can now establish a connection to the desired website.

### Python Code Demonstration:

Here's a simple Python script that demonstrates DNS resolution using the `socket` module:

```python
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
```

This Python script uses the `gethostbyname()` function from the `socket` module to resolve the IP address of a domain name. You can replace `'example.com'` with any domain name you want to resolve.

Save this code in a Python script file, for example, `dns_resolution.py`, and run it using Python. It will print the IP address associated with the specified domain name.