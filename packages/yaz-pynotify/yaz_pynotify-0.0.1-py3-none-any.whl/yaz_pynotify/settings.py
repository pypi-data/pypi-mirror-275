class EmailSetting:
    """
    A class to represent the settings required for email configuration.

    Attributes:
        port (int): The port number for the SMTP server.
        host (str): The host address of the SMTP server.
        username (str): The username for the SMTP server authentication.
        password (str): The password for the SMTP server authentication.
    """
    def __init__(self, port: int, host: str, username: str, password: str) -> None:
        """
        Constructs all the necessary attributes for the EmailSetting object.

        Args:
            port (int): The port number for the SMTP server.
            host (str): The host address of the SMTP server.
            username (str): The username for the SMTP server authentication.
            password (str): The password for the SMTP server authentication.
        """
        self.port = port
        self.host = host
        self.username = username
        self.password = password


class SMSSetting:
    """
    A class to represent the settings required for SMS configuration.

    Attributes:
        api_key (str): The API key for the SMS service.
        api_pwd (str): The API password for the SMS service.
        url (str): The URL endpoint for the SMS service.
    """
    def __init__(self, api_key: str, api_pwd: str, url: str) -> None:
        """
        Constructs all the necessary attributes for the SMSSetting object.

        Args:
            api_key (str): The API key for the SMS service.
            api_pwd (str): The API password for the SMS service.
            url (str): The URL endpoint for the SMS service.
        """
        self.api_key = api_key
        self.api_pwd = api_pwd
        self.url = url


class Settings:
    """
    A class to hold and manage SMS and email settings.

    Attributes:
        sms_settings (SMSSetting): The SMS settings.
        email_settings (EmailSetting): The email settings.
    """

    sms_settings: SMSSetting |None
    email_settings: EmailSetting |None

    @staticmethod
    def set(sms_settings: SMSSetting|None=None, email_settings: EmailSetting|None=None) -> None:
        """
        Static method to set the SMS and email settings.

        Args:
            sms_settings (SMSSetting): The SMS settings.
            email_settings (EmailSetting): The email settings.
        """
        Settings.sms_settings = sms_settings
        Settings.email_settings = email_settings
