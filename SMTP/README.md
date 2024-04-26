### How SMTP Works:

SMTP is a protocol used for sending email messages between servers. It works in conjunction with other protocols such as POP3 or IMAP which are used for retrieving emails from a mail server.

1. **Connection Establishment**: The client (sender's mail server) initiates a TCP connection with the recipient's mail server on port 25, the default port for SMTP.

2. **Handshake**: Once the connection is established, a handshake process occurs where the client and server exchange information about the supported SMTP commands and negotiate the parameters of the email transmission.

3. **Message Transfer**: The sender then sends the email message to the recipient's mail server using SMTP commands such as HELO, MAIL FROM, RCPT TO, DATA, and QUIT. These commands specify the sender, recipient, and content of the email.

4. **Delivery**: The recipient's mail server processes the incoming email, performs spam filtering, and delivers the message to the recipient's mailbox.

5. **Closure**: Finally, the SMTP connection is closed either by the client or the server.

### Python Code Example:

Here's a simple Python code example demonstrating how to send an email using SMTP:

1. **Generate Application-Specific Password**:
   - Go to your Google Account settings: [Google Account Settings](https://myaccount.google.com/security).
   - Under "Signing in to Google," click on "App passwords" (you might need to sign in again).
   - If prompted, enter your Google account password.
   - Scroll down to the "App passwords" section.
   - Select "Mail" as the app and "Other (Custom name)" as the device.
   - Enter a custom name for your Python script (e.g., "Python SMTP Script").
   - Click on "Generate".
   - Google will generate an application-specific password for you. Copy this password.
   - Use this generated password instead of your regular Google account password in your Python script.

   If you don't see the option for app-specific passwords go to: https://myaccount.google.com/apppasswords, you may need to create one by selecting the options from the drop-down boxes and then clicking the "Generate" button. The steps are explained [here](https://support.google.com/accounts/answer/185833?hl=en).

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
sender_email = "your_email@gmail.com"
receiver_email = "recipient_email@gmail.com"
password = "your_password" #Replace Application-Specific Password Here
subject = "Test Email"
body = "This is a test email sent using Python."

# Create a MIMEText object to represent the email body
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))

# Connect to the SMTP server (e.g., Gmail's SMTP server)
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender_email, password)

# Send the email
server.sendmail(sender_email, receiver_email, message.as_string())

# Close the connection
server.quit()

print("Email sent successfully!")
```

Before running the code, make sure to replace `"your_email@gmail.com"`, `"recipient_email@gmail.com"`, and `"your_password"` with your own Gmail email address, recipient's email address, and Gmail password, respectively. Also, ensure that your Gmail account allows access for less secure apps or use an App Password if you have 2-factor authentication enabled.

Save the code in a Python file (e.g., `send_email.py`) and execute it using Python. It will send an email from your Gmail account to the specified recipient.