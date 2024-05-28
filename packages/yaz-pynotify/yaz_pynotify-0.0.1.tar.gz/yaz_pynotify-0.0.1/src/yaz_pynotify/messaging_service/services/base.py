from abc import ABC,abstractmethod
from ...messaging_service.types import MessageData
from ...settings import Settings

class MessagingService(ABC):
    settings = Settings
    @abstractmethod
    def send(self, data:MessageData):
        raise NotImplementedError("send method not implemented!")