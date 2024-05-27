from .models import Task


def start_callback_service(service, *args, **kwargs):
    return Task.delay(service, *args, **kwargs)
