import logging
from django.db import models
from django.db import transaction
from django.utils import timezone
from django_model_helper.models import WithAddModTimeFields
from django_model_helper.models import WithDeletedStatusFields
from django_model_helper.models import WithUidFields
from django_model_helper.models import WithSimpleNRRDStatusFields
from django_model_helper.models import WithArgsKwargsFields
from django_model_helper.models import WithSimpleResultFields

from .utils import get_celery_callback_service_url
from .settings import CELERY_CALLBACK_SERVICE_APIKEYS
from .celery_tasks import celery_callback_service_execute_start

_logger = logging.getLogger(__name__)


class Task(
    WithAddModTimeFields,
    WithDeletedStatusFields,
    WithUidFields,
    WithArgsKwargsFields,
    WithSimpleResultFields,
):
    execution_lock_timeout = models.IntegerField(
        default=60,
        verbose_name="任务执行锁定时长",
    )
    service = models.CharField(
        max_length=512,
        verbose_name="服务函数",
    )
    celery_task_id = models.CharField(
        max_length=64,
        null=True,
        blank=True,
        verbose_name="Celery任务ID",
    )
    celery_task_start_time = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Celery任务创建时间",
    )

    class Meta:
        permissions = [
            ("restart_celery_callback_service", "允许重新向Celery推送"),
        ] + WithDeletedStatusFields.Meta.permissions
        verbose_name = "回调任务"
        verbose_name_plural = "回调任务"

    def __str__(self):
        return self.uid

    def start_celery_callback_service(self, delay_seconds=5, save=True):
        url = get_celery_callback_service_url()
        apikey = CELERY_CALLBACK_SERVICE_APIKEYS[0]
        task = {
            "url": url,
            "apikey": apikey,
            "uid": self.uid,
        }
        _logger.debug(
            "start_celery_callback_service, url=%s, apikey=%s, uid=%s",
            url,
            apikey,
            task,
        )
        async_result = celery_callback_service_execute_start(
            task,
            delay_seconds=delay_seconds,
        )
        self.celery_task_id = async_result.task_id
        self.celery_task_start_time = timezone.now()
        if save:
            self.save()

    @classmethod
    def delay(cls, service, *args, **kwargs):
        execution_lock_timeout = 60
        delay_seconds = 5
        if callable(service):
            execution_lock_timeout = getattr(service, "execution_lock_timeout", 60)
            delay_seconds = getattr(service, "delay_seconds", 5)
            service = ".".join([service.__module__, service.__name__])
        inst = cls()
        inst.execution_lock_timeout = execution_lock_timeout
        inst.service = service
        inst.args = args
        inst.kwargs = kwargs
        inst.save()
        inst.start_celery_callback_service(delay_seconds=delay_seconds)
        return inst
