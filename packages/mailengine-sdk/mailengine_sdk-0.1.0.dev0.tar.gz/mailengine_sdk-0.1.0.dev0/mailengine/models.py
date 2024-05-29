class Email:
    def __init__(self, recipient_email, recipient_name, sender_email, sender_name, subject, content):
        """
        Initialize an Email object.

        :param recipient_email: Email address of the recipient.
        :param recipient_name: Name of the recipient.
        :param sender_email: Email address of the sender.
        :param sender_name: Name of the sender.
        :param subject: Subject of the email.
        :param content: Content of the email.
        """
        self.recipient_email = recipient_email
        self.recipient_name = recipient_name
        self.sender_email = sender_email
        self.sender_name = sender_name
        self.subject = subject
        self.content = content
