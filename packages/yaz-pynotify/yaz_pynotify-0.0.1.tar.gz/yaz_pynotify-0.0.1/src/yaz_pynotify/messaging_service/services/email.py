from ...messaging_service.services.base import MessagingService
from ...messaging_service.types import MessageData
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class SMTPClient:
    def __init__(self, host, port, user, password):
        self.server = host
        self.port = port
        self.user = user
        self.password = password
        self.connection = None

    def connect(self):
        self.connection = smtplib.SMTP(self.server, self.port)
        self._secure_connection()  # Secure the connection
        self._login()  # Login to the SMTP server

    def _secure_connection(self):
        if self.connection:
            try:
                self.connection.starttls()
            except smtplib.SMTPHeloError:
                raise ConnectionError("Helo greeting failed")

    def _login(self):
        if self.connection:
            try:
                self.connection.login(self.user, self.password)
            except smtplib.SMTPHeloError:
                raise ConnectionError("Helo greeting failed")
            except smtplib.SMTPAuthenticationError:
                raise smtplib.SMTPAuthenticationError(code=401, msg="Authentication failed! Invalid authentication credentials")
            except smtplib.SMTPNotSupportedError:
                raise smtplib.SMTPNotSupportedError(code=500, msg="SMTP Not Supported")
            except smtplib.SMTPException:
                raise ConnectionError("Unknown authentication error")
            
    def disconnect(self):
        if self.connection:
            try:
                self.connection.quit()
            except smtplib.SMTPServerDisconnected:
                pass
            
    def send_email(self, recipient: str, subject: str, body: str, is_html: bool = False):
        if not self.connection:
            raise ConnectionError("SMTP connection not established. Call connect() first.")
        
        try:
            msg = MIMEMultipart()
            msg['From'] = self.user
            msg['To'] = recipient
            msg['Subject'] = subject

            msg.attach(MIMEText(body, 'html' if is_html else 'plain'))

            self.connection.send_message(msg)

        except Exception as e:
            raise RuntimeError(f"Error sending email: {e}")

    def __del__(self):
        self.disconnect()


class EmailMessagingService(MessagingService):
    smtp = None

    def __init__(self) -> None:
        self.config = getattr(self.settings, "email_settings", None)
        
        if self.config is None:
            raise NotImplementedError("No configuration provided for email service")
    
        self._smtp = self.configure_smtp()
        
    def configure_smtp(self):
        if EmailMessagingService.smtp is None:
            EmailMessagingService.smtp = SMTPClient(
                host=self.config.host, 
                port=self.config.port, 
                user=self.config.username, 
                password=self.config.password
            )
            EmailMessagingService.smtp.connect()
        return EmailMessagingService.smtp

    def send(self, data: MessageData):
        self._smtp.send_email(
                recipient=data.recipient, 
                subject=data.subject, 
                body=data.body,
                is_html=data.is_html
            )
    
    def __del__(self):
        if EmailMessagingService.smtp:
            EmailMessagingService.smtp.disconnect()
