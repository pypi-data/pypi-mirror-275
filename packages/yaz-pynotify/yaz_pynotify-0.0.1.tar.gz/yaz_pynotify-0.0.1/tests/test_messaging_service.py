import pytest 
from unittest.mock import patch, Mock
from src.yaz_pynotify.messaging_service.types import MessageData
from src.yaz_pynotify.settings import Settings
from src.yaz_pynotify.messaging_service.services.email import EmailMessagingService
from src.yaz_pynotify.messaging_service.services.sms import SMSMessagingService 

def test_smtp_connect(smtp_client):
    with patch('smtplib.SMTP') as mock_smtp:
        mock_connection = Mock()
        mock_smtp.return_value = mock_connection
        
        smtp_client.connect()
        mock_connection.starttls.assert_called_once()
        mock_connection.login.assert_called_once_with("user@example.com", "password")

def test_smtp_send_email(smtp_client):
    smtp_client.connection = Mock()
    recipient = "recipient@example.com"
    subject = "Test Subject"
    body = "Test Body"

    smtp_client.send_email(recipient, subject, body)
    smtp_client.connection.send_message.assert_called_once()

def test_email_messaging_service_no_config():
    class MockSettings:
        email_settings = None

    with patch.object(Settings, 'email_settings', MockSettings.email_settings):
        with pytest.raises(NotImplementedError):
            EmailMessagingService()

def test_email_messaging_service():
    mock_email_settings = Mock(host="smtp.example.com", port=587, username="user@example.com", password="password")
    mock_smtp_client = Mock()

    with patch.object(Settings, 'email_settings', mock_email_settings), \
         patch('src.yaz_pynotify.messaging_service.services.email.SMTPClient', return_value=mock_smtp_client):
        service = EmailMessagingService()
        assert service._smtp is not None
        mock_smtp_client.connect.assert_called_once()

def test_email_messaging_service_send():
    class MockSettings:
        email_settings = Mock(host="smtp.example.com", port=587, username="user@example.com", password="password")

    with patch.object(Settings, 'email_settings', MockSettings.email_settings):
        service = EmailMessagingService()
        service._smtp = Mock()
        data = MessageData(recipient="recipient@example.com", subject="Test Subject", body="Test Body", is_html=False)
        
        service.send(data)
        service._smtp.send_email.assert_called_once_with(
            recipient="recipient@example.com",
            subject="Test Subject",
            body="Test Body",
            is_html=False
        )

def test_sms_messaging_service_no_config():
    class MockSettings:
        sms_settings = None

    with patch.object(Settings, 'sms_settings', MockSettings.sms_settings):
        with pytest.raises(NotImplementedError):
            SMSMessagingService()

def test_sms_messaging_service_send():
    class MockSettings:
        sms_settings = Mock()

    with patch.object(Settings, 'sms_settings', MockSettings.sms_settings):
        service = SMSMessagingService()
        with pytest.raises(NotImplementedError):
            service.send(MessageData(recipient="1234567890", subject="", body="Test Message", is_html=False))
