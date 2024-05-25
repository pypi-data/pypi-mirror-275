import time
from django.test import LiveServerTestCase
from celery_callback_service import settings
from celery_callback_service.client import start_callback_service


def ping():
    return "pong"


ping.delay_seconds = 1


class TestCeleryCallbackService(LiveServerTestCase):
    def setUp(self):
        settings.CELERY_CALLBACK_SERVICE_ADDRESS = self.live_server_url

    def test1(self):
        task = start_callback_service(ping)
        assert task.success is None

        time.sleep(3)

        task.refresh_from_db()
        assert task.success
