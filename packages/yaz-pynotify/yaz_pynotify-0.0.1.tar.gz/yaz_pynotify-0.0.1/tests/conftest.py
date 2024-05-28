import pytest 
from src.yaz_pynotify.messaging_service.services.email import SMTPClient
from src.yaz_pynotify.settings import Settings

Settings.set()

@pytest.fixture
def smtp_client():
    return SMTPClient(host="smtp.example.com", port=587, user="user@example.com", password="password")
