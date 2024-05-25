import urllib

from django.urls import reverse
from django.conf import settings

from . import constants
from . import settings


def get_celery_callback_service_url():
    path = reverse(constants.CELERY_CALLBACK_SERVICE_VIEW_NAME)
    return urllib.parse.urljoin(settings.CELERY_CALLBACK_SERVICE_ADDRESS, path)
