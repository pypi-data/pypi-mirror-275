from ...messaging_service.services.base import MessagingService
from ...messaging_service.types import MessageData


class SMSMessagingService(MessagingService):
    def __init__(self) -> None:
        if not getattr(self.settings, "sms_settings", False):
            raise NotImplementedError("No configuration provided for sms service")
        
    def send(self, data: MessageData):
        raise NotImplementedError("Sms Service has not been implemented yet!")