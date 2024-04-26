import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
sender_email = "your_email@gmail.com"
receiver_email = "receiver_email@gmail.com"
password = "mnop ijkl efgh abcd"
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
