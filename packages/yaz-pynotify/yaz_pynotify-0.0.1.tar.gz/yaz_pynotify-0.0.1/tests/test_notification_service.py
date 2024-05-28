import pytest
from unittest.mock import Mock, patch
from src.yaz_pynotify.notification_service.handlers.base import NotificationHandler, NotificationHandlerRegistry,  MessageData
from src.yaz_pynotify.notification_service.handlers.email import EmailHandler  # Replace 'your_module' with the actual module name
from src.yaz_pynotify.notification_service.handlers.sms import SMSHandler
from src.yaz_pynotify.messaging_service.factory import ServiceFactory  # Replace 'your_module' with the actual module name

class TestNotificationHandler(NotificationHandler):
    def handle(self, kind: str, data: MessageData):
        pass

def test_notification_handler_set_next():
    handler1 = TestNotificationHandler()
    handler2 = TestNotificationHandler()
    handler1.set_next(handler2)
    assert handler1.next == handler2

def test_notification_handler_forward_responsibility():
    handler1 = TestNotificationHandler()
    handler2 = Mock()
    handler1.set_next(handler2)
    data = MessageData(recipient="test@example.com", subject="Test", body="Test Body", is_html=False)
    handler1.forwardResponsibility(kind="email", data=data)
    handler2.handle.assert_called_once_with("email", data)

def test_notification_handler_registry_register():
    handler1 = TestNotificationHandler()
    handler2 = TestNotificationHandler()
    NotificationHandlerRegistry.register(handler1)
    NotificationHandlerRegistry.register(handler2)
    assert NotificationHandlerRegistry.handlers == [handler1, handler2]
    assert handler2.next == handler1

def test_notification_handler_registry_get_root():
    handler1 = TestNotificationHandler()
    handler2 = TestNotificationHandler()
    NotificationHandlerRegistry.register(handler1)
    NotificationHandlerRegistry.register(handler2)
    assert NotificationHandlerRegistry.getRoot() == handler2

def test_notification_handler_registry_no_handlers():
    NotificationHandlerRegistry.handlers = []
    with pytest.raises(ValueError, match="No Register Handler"):
        NotificationHandlerRegistry.getRoot()

@patch.object(ServiceFactory, 'createMessagingService')
def test_email_handler_handle(mock_create_service):
    mock_email_service = Mock()
    mock_create_service.return_value = mock_email_service
    handler = EmailHandler()
    data = MessageData(recipient="test@example.com", subject="Test", body="Test Body", is_html=False)
    handler.handle(kind="email", data=data)
    mock_create_service.assert_called_once_with("email")
    mock_email_service.send.assert_called_once_with(data)

@patch.object(ServiceFactory, 'createMessagingService')
def test_email_handler_forward_responsibility(mock_create_service):
    handler = EmailHandler()
    next_handler = Mock()
    handler.set_next(next_handler)
    data = MessageData(recipient="test@example.com", subject="Test", body="Test Body", is_html=False)
    handler.handle(kind="sms", data=data)
    next_handler.handle.assert_called_once_with("sms", data)

@patch.object(ServiceFactory, 'createMessagingService')
def test_sms_handler_handle(mock_create_service):
    mock_sms_service = Mock()
    mock_create_service.return_value = mock_sms_service
    handler = SMSHandler()
    data = MessageData(recipient="1234567890", subject="Test", body="Test Body", is_html=False)
    handler.handle(kind="sms", data=data)
    mock_create_service.assert_called_once_with("sms")
    mock_sms_service.send.assert_called_once_with(data)

@patch.object(ServiceFactory, 'createMessagingService')
def test_sms_handler_forward_responsibility(mock_create_service):
    handler = SMSHandler()
    next_handler = Mock()
    handler.set_next(next_handler)
    data = MessageData(recipient="1234567890", subject="Test", body="Test Body", is_html=False)
    handler.handle(kind="email", data=data)
    next_handler.handle.assert_called_once_with("email", data)
