from ..notification_service.config import getNotificationHandler
from ..messaging_service.types import MessageData

def notify(kind: str, data: MessageData):
    """
    Notify the recipient based on the specified kind and message data.

    Args:
        kind (str): The type of notification to send, either "email" or "sms".
        data (MessageData): The data for the message to be sent.
    """
    handler = getNotificationHandler()
    handler.handle(kind, data)