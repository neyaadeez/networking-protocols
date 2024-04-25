### How FTP Works

FTP is a standard network protocol used for transferring files between a client and a server on a TCP/IP network, such as the internet. It operates on the application layer of the OSI model and typically uses port 21 for control information and port 20 for data transmission.

The FTP protocol involves two main phases:

1. **Control Connection Establishment**: 
   - The client initiates a control connection to the server on port 21.
   - Once the control connection is established, the client sends FTP commands to the server to perform various operations such as login, change directory, list directory contents, upload files, and download files.

2. **Data Transfer**:
   - For file transfer operations (e.g., upload/download), a separate data connection is established.
   - Data can be transferred in two modes: active mode and passive mode.
   - In active mode, the server initiates a data connection to the client on port 20.
   - In passive mode, the client initiates a data connection to the server, and the server listens on a random port for the incoming data connection.

### Python Implementation

Here's a simple Python code to demonstrate FTP file upload and download using the `ftplib` module:

```python
import ftplib

def ftp_upload(hostname, username, password, local_file, remote_dir):
    try:
        # Connect to FTP server
        ftp = ftplib.FTP(hostname)
        ftp.login(username, password)
        
        # Change to the remote directory
        ftp.cwd(remote_dir)
        
        # Open local file for uploading
        with open(local_file, 'rb') as file:
            ftp.storbinary(f'STOR {local_file}', file)
        
        print(f"File '{local_file}' uploaded successfully to '{remote_dir}'")
    except ftplib.all_errors as e:
        print(f"FTP error: {e}")

def ftp_download(hostname, username, password, remote_file, local_dir):
    try:
        # Connect to FTP server
        ftp = ftplib.FTP(hostname)
        ftp.login(username, password)
        
        # Change to the remote directory
        ftp.cwd(local_dir)
        
        # Open local file for downloading
        with open(remote_file, 'wb') as file:
            ftp.retrbinary(f'RETR {remote_file}', file.write)
        
        print(f"File '{remote_file}' downloaded successfully to '{local_dir}'")
    except ftplib.all_errors as e:
        print(f"FTP error: {e}")

# Example usage
ftp_upload('ftp://bck-speedtest-1.tele2.net/', 'username', 'password', 'local_file.txt', '/upload')
ftp_download('ftp.example.com', 'username', 'password', 'remote_file.txt', 'local_directory')
```

This code demonstrates how to upload a local file to a remote FTP server and download a file from the FTP server to a local directory using Python's `ftplib` module. Make sure to replace `'ftp.example.com'`, `'username'`, `'password'`, `'local_file.txt'`, `'remote_directory'`, `'remote_file.txt'`, and `'local_directory'` with your actual FTP server details and file paths.

Read: https://stackoverflow.com/a/29104430