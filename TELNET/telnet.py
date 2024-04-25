import telnetlib

# Define the remote host and port
host = 'example.com'
port = 23

# Create a Telnet connection
try:
    tn = telnetlib.Telnet(host, port)
    print("Connected to", host)

    # Login (if required)
    tn.read_until(b"login: ")
    tn.write(b"your_username\n")
    tn.read_until(b"Password: ")
    tn.write(b"your_password\n")

    # Execute commands
    tn.write(b"ls\n")  # Example command: list directory contents
    output = tn.read_all().decode('ascii')
    print(output)

    # Close the connection
    tn.close()
    print("Connection closed")
except ConnectionRefusedError:
    print("Connection to", host, "refused")
except Exception as e:
    print("An error occurred:", e)