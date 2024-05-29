from mailengine import MailEngine
from mailengine.models import Email

# Replace the bearer token with your own (without Bearer prefix)
bearer_token = "<YOUR_BEARER_TOKEN_HERE>"

# Create an instance of MailEngine with the bearer token
client = MailEngine(bearer_token)

# Create an Email object
email = Email(
    recipient_email="recipient@example.com",
    recipient_name="Recipient Name",
    sender_email="sender@example.com",
    sender_name="Sender Name",
    subject="A letter to Houston",
    content="Hello, World!"
)

# Send the email
try:
    response = client.send_email(email)
    print("Email sent successfully:", response)
except Exception as e:
    print("Failed to send email:", e)
