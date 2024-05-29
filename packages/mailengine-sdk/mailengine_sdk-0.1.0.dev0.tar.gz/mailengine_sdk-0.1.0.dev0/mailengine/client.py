import requests
from .models import Email

class MailEngine:
    def __init__(self, bearer_token, base_url="https://mailengine.umbratic.com/api"):
        """
        Initialize the MailEngine.

        :param bearer_token: Bearer token for authorization.
        :param base_url: Base URL of the MailEngine API.
        """
        self.base_url = base_url
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {bearer_token}"
        }

    def send_email(self, email):
        """
        Send an email using the MailEngine API.

        :param email: An Email object containing email details.
        :return: Response JSON from the API.
        """
        url = f"{self.base_url}/send-email"
        payload = {
            "recipientEmail": email.recipient_email,
            "recipientName": email.recipient_name,
            "senderEmail": email.sender_email,
            "senderName": email.sender_name,
            "emailSubject": email.subject,
            "emailContent": email.content
        }
        try:
            response = requests.post(url, json=payload, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            try:
                error_code = response.status_code
                error_msg = response.json().get("error")
                error_detail = response.json().get("message")
            except Exception:
                error_code = None
                error_msg = "Unknown error"
                error_detail = "No error message provided"
            raise MailEngineError(f"Failed to send email. Error code: {error_code}. Error: {error_msg}. Details: {error_detail}")

class MailEngineError(Exception):
    """
    Custom exception class for MailEngine errors.
    """
    pass
