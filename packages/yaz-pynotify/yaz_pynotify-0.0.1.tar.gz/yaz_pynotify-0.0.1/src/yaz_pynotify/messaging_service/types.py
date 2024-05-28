class MessageData:
    """
    A class to represent the data required for sending a message.

    Attributes:
        recipient (str): The recipient of the message.
        subject (str | None): The subject of the message (optional for SMS).
        body (str): The body content of the message.
        is_html (bool): Indicates if the message body is in HTML format.
    """
    def __init__(self, recipient: str, subject: str | None, body: str, is_html: bool = False) -> None:
        """
        Constructs all the necessary attributes for the MessageData object.

        Args:
            recipient (str): The recipient of the message.
            subject (str | None): The subject of the message (optional for SMS).
            body (str): The body content of the message.
            is_html (bool, optional): Indicates if the message body is in HTML format. Defaults to False.
        """
        self.recipient = recipient
        self.subject = subject
        self.body = body
        self.is_html = is_html

    def __repr__(self) -> str:
        """
        Provides a string representation of the MessageData object.

        Returns:
            str: A string representation of the recipient and the message body.
        """
        return f"{self.recipient}: {self.body}"