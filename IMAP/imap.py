import imaplib
import ssl

# IMAP server settings
IMAP_SERVER = 'imap.gmail.com'
USERNAME = 'your_mail@gmail.com'
PASSWORD = 'mnop ijkl efgh abcd'

# Create an SSL context
ssl_context = ssl.create_default_context()

# Connect to the IMAP server with SSL encryption
imap = imaplib.IMAP4_SSL(IMAP_SERVER, port=993, ssl_context=ssl_context)

# Login to the server
imap.login(USERNAME, PASSWORD)

# Select a mailbox (e.g., Inbox)
mailbox = 'INBOX'
imap.select(mailbox)

# Search for all unseen (unread) emails
status, data = imap.search(None, 'UNSEEN')

if status == 'OK':
    # Iterate through the list of email IDs
    for num in data[0].split():
        # Fetch the email by its ID
        status, msg_data = imap.fetch(num, '(RFC822)')
        if status == 'OK':
            # Print the email content
            print('Message:', msg_data[0][1])
        else:
            print('Error fetching message:', status)

# Logout and close the connection
imap.logout()