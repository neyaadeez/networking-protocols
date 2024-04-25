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
ftp_upload('bck-speedtest-1.tele2.net', 'anonymous', 'password', 'local_file.txt', '/upload')
ftp_download('ftp.example.com', 'username', 'password', 'remote_file.txt', 'local_directory')