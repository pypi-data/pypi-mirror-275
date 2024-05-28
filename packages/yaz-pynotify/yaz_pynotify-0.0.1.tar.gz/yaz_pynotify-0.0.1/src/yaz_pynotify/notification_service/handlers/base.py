from abc import ABC, abstractmethod
from ...messaging_service.types import MessageData
from typing import Optional
class NotificationHandler(ABC):
    """
    Abstract base class for notification handlers in the chain of responsibility pattern.

    Attributes:
        next (NotificationHandler | None): The next handler in the chain of responsibility.
    """

    next: Optional['NotificationHandler'] = None

    def set_next(self, handler: 'NotificationHandler'):
        """
        Sets the next handler in the chain of responsibility.

        Args:
            handler (NotificationHandler): The next handler to set.
        """
        self.next = handler

    @abstractmethod
    def handle(self, kind: str, data: MessageData):
        """
        Abstract method to handle the notification based on the specified kind and message data.

        Args:
            kind (str): The type of notification to handle.
            data (MessageData): The data for the message to be sent.

        Raises:
            ValueError: If no handler is registered for the specified kind.
        """
        raise ValueError(f"No registered handler for kind: {kind}")
    
    def forwardResponsibility(self, kind: str, data: MessageData):
        """
        Forwards the handling responsibility to the next handler in the chain.

        Args:
            kind (str): The type of notification to send, either "email" or "sms".
            data (MessageData): The data for the message to be sent.

        Raises:
            ValueError: If there is no registered handler for the given kind.
        """
        if self.next:
            self.next.handle(kind, data)
        else:
            raise ValueError(f"No registered handler for kind: {kind}")


class NotificationHandlerRegistry:
    """
    A registry to manage notification handlers and their chaining.

    Attributes:
        handlers (list[NotificationHandler]): The list of registered notification handlers.
    """

    handlers: list[NotificationHandler] = []

    @staticmethod
    def has_handlers():
        return len(NotificationHandlerRegistry.handlers) > 0

    @staticmethod
    def register(handler: NotificationHandler):
        """
        Registers a new notification handler and sets it as the next handler
        in the chain of responsibility for the previously registered handler.

        Args:
            handler (NotificationHandler): The handler to register.
        """

        
        if NotificationHandlerRegistry.has_handlers():
            handler.set_next(NotificationHandlerRegistry.handlers[-1])

        NotificationHandlerRegistry.handlers.append(handler)
 
    @staticmethod
    def getRoot():
        if NotificationHandlerRegistry.has_handlers():
            return NotificationHandlerRegistry.handlers[-1]
        
        raise ValueError("No Register Handler")