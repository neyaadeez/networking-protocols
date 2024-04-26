### How POP3 Works:
POP3 is a protocol used by email clients to retrieve email messages from a mail server. Here's a simplified overview of how it works:

1. **Connection Establishment**: The email client establishes a TCP connection with the POP3 server on port 110 or 995 (for POP3S, the secure version which uses SSL/TLS).

2. **Authentication**: Once the connection is established, the client sends the username and password to the server for authentication.

3. **Transaction Phase**: After successful authentication, the client can issue commands to the server to manage emails. Common commands include:
   - `LIST`: Get a list of email messages and their sizes.
   - `RETR`: Retrieve a specific email message by its index number.
   - `DELE`: Delete a specific email message.
   - `QUIT`: End the session and close the connection.

4. **Download Emails**: The client retrieves email messages from the server using the `RETR` command. The server responds with the content of the requested email.

5. **Deletion**: If the client issues the `DELE` command for any email messages, they are marked for deletion but not immediately removed from the server. They are only removed when the client terminates the session using the `QUIT` command.

6. **Closing Connection**: The client ends the session by sending the `QUIT` command. The server closes the connection and any messages marked for deletion are removed permanently.

### Python Code Example:
Here's a simple Python code example demonstrating how to retrieve emails from a POP3 server using the `poplib` module:

### Retrieving Emails from a POP3 Server using Python

To retrieve emails from a POP3 server in Python, you need to generate an application-specific password for your script, especially if you're using services like Gmail. Here's how you can do it:

1. **Generate Application-Specific Password**:
   - Go to your Google Account settings: [Google Account Settings](https://myaccount.google.com/security).
   - Under "Signing in to Google," click on "App passwords" (you might need to sign in again).
   - If prompted, enter your Google account password.
   - Scroll down to the "App passwords" section.
   - Select "Mail" as the app and "Other (Custom name)" as the device.
   - Enter a custom name for your Python script (e.g., "Python POP3 Script").
   - Click on "Generate".
   - Google will generate an application-specific password for you. Copy this password.
   - Use this generated password instead of your regular Google account password in your Python script.

   If you don't see the option for app-specific passwords go to: https://myaccount.google.com/apppasswords, you may need to create one by selecting the options from the drop-down boxes and then clicking the "Generate" button. The steps are explained [here](https://support.google.com/accounts/answer/185833?hl=en).

2. **Set up POP**
    - On your computer, open Gmail.
    - In the top right, click Settings Settings and then See all settings.
    - Click the Forwarding and POP/IMAP tab.
    - In the "POP download" section, select Enable POP for all mail or Enable POP for mail that arrives from now on.
    - At the bottom of the page, click Save Changes.
    - Read: https://support.google.com/mail/answer/7104828?hl=en

2. **Python Script to Retrieve Emails**:

```python
import poplib
import ssl
from email.parser import Parser

# POP3 server settings for Gmail
pop3_server = 'pop.gmail.com'
port = 995
username = 'your_email@gmail.com' # Replace your user-name and password
password = 'your_application_specific_password'  # Use the generated application-specific password here

# Connect to the POP3 server with SSL/TLS
context = ssl.create_default_context()
pop3 = poplib.POP3_SSL(pop3_server, port, context=context)

# Authenticate
pop3.user(username)
pop3.pass_(password)

# Get mailbox statistics
num_messages, total_size = pop3.stat()
print("Total emails:", num_messages)

# Retrieve email messages
for i in range(1, num_messages + 1):
    response, lines, bytes = pop3.retr(i)
    email_content = b'\n'.join(lines)
    # Parse email content using email.parser.Parser
    msg_content = Parser().parsestr(email_content.decode('utf-8'))
    # Print subject and from fields
    print("Email", i, "Subject:", msg_content['subject'])
    print("From:", msg_content['from'])
    # Print email body
    print("Email", i, "Body:")
    print(msg_content.get_payload())

# Close the connection
pop3.quit()
```
Replace 'your_application_specific_password' with the generated application-specific password obtained from your Google Account settings. This should allow your Python script to authenticate successfully with the Gmail POP3 server.