from ..messaging_service.services import base, email, sms

class ServiceFactory:
    """
    A factory class to create messaging service instances based on the provided kind.

    Methods:
        createMessagingService(kind: str) -> base.MessagingService:
            Creates and returns an instance of the specified messaging service.
    """
    
    @staticmethod
    def createMessagingService(kind: str) -> base.MessagingService:
        """
        Creates and returns an instance of the specified messaging service.

        Args:
            kind (str): The type of messaging service to create, either "email" or "sms".

        Returns:
            base.MessagingService: An instance of the specified messaging service.

        Raises:
            ValueError: If the provided kind is not a valid messaging service type.
        """
        match(kind):
            case "email":
                return email.EmailMessagingService()
            case "sms":
                return sms.SMSMessagingService()
        
        raise ValueError(f"{kind} is not a valid Messaging Service")
