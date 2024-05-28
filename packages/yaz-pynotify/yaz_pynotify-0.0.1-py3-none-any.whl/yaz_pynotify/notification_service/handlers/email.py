from ...messaging_service.types import MessageData
from ...notification_service.handlers.base import NotificationHandler
from ...messaging_service.factory import ServiceFactory

class EmailHandler(NotificationHandler):
    """
    A handler class to process email notifications.

    Attributes:
        kind (str): The type of notification this handler processes ("email").
        next (NotificationHandler | None): The next handler in the chain of responsibility.
    """
    
    kind = "email"
    next: NotificationHandler | None = None

    def set_next(self, handler: NotificationHandler):
        """
        Sets the next handler in the chain of responsibility.

        Args:
            handler (NotificationHandler): The next handler to set.
        """
        self.next = handler

    def handle(self, kind: str, data: MessageData):
        """
        Handles the notification based on the specified kind and message data.

        If the kind matches "email", it uses the email service to send the message.
        Otherwise, it passes the handling to the next handler in the chain.

        Args:
            kind (str): The type of notification to handle.
            data (MessageData): The data for the message to be sent.

        Returns:
            The result of the email service send operation or the next handler's handle method.

        Raises:
            Any exception raised by the email service send operation or the next handler's handle method.
        """
        if kind == self.kind:
            email_service = ServiceFactory.createMessagingService(self.kind)
            return email_service.send(data)
        else:
            return self.forwardResponsibility(kind=kind, data=data)
        
