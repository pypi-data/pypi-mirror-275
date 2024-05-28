
from ..notification_service.handlers.base import NotificationHandlerRegistry
from ..notification_service.handlers.email import EmailHandler
from ..notification_service.handlers.sms import SMSHandler

NotificationHandlerRegistry.register(EmailHandler())
NotificationHandlerRegistry.register(SMSHandler())

def getNotificationHandler():
    """
    Retrieves the configured notification handler chain.

    Returns:
        The root handler of the notification handler chain.
    """
    return NotificationHandlerRegistry.getRoot()
