import paramiko

# SSH connection parameters
hostname = 'your_server_hostname'
port = 22
username = 'your_username'
password = 'your_password'

# Create SSH client instance
ssh_client = paramiko.SSHClient()

# Automatically add host keys without requiring user confirmation
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Connect to the SSH server
    ssh_client.connect(hostname, port, username, password)

    # Execute a command on the remote server
    stdin, stdout, stderr = ssh_client.exec_command('ls -l')

    # Read and print the command output
    print("Command Output:")
    for line in stdout:
        print(line.strip())

except Exception as e:
    print("An error occurred:", e)

finally:
    # Close the SSH connection
    ssh_client.close()