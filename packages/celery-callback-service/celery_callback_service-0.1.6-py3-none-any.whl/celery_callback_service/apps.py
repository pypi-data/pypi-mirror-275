from django.apps import AppConfig


class CeleryCallbackServiceConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "celery_callback_service"
    verbose_name = "基于Celery的回调服务"
