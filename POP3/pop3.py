import poplib
import ssl
from email.parser import Parser

# POP3 server settings for Gmail
pop3_server = 'pop.gmail.com'
port = 995
username = 'xyz@gmail.com'
password = 'mnop ijkl efgh abcd'

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
