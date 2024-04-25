import requests

# SIP server details
sip_server = "sip.example.com"
sip_port = 5060

# Sender and recipient SIP addresses
sender_uri = "sip:alice@example.com"
recipient_uri = "sip:bob@example.com"

# Construct SIP INVITE request
invite_request = f"INVITE {recipient_uri} SIP/2.0\r\n" \
                 f"Via: SIP/2.0/UDP {sip_server}:{sip_port}\r\n" \
                 f"From: {sender_uri}\r\n" \
                 f"To: {recipient_uri}\r\n" \
                 f"Content-Length: 0\r\n\r\n"

# Send SIP INVITE request
response = requests.request("INVITE", f"http://{sip_server}:{sip_port}", data=invite_request)

# Print SIP server response
print("SIP Server Response:")
print(response.text)