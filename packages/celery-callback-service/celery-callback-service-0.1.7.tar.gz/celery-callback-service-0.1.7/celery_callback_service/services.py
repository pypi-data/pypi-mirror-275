import logging
from zenutils import importutils
from django_apis.exceptions import BusinessError
from globallock.django import get_default_global_lock_manager
from .models import Task


_global_lock_manager = get_default_global_lock_manager()
_logger = logging.getLogger(__name__)


def celery_callback_service(uid):
    """回调任务调度器。"""
    try:
        task = Task.objects.get(uid=uid)
    except Task.DoesNotExist:
        msg = f"callback task {uid} not found..."
        _logger.warning(msg)
        raise BusinessError(msg)
    if task.success is not None:
        # 任务已经执行
        # 无须更新任务数据
        # 可以直接抛出异常以结束本次回调
        msg = f"callback task {task.uid} already finished..."
        _logger.warning(msg)
        raise BusinessError(msg)

    lock_key = f"celery_callback_service:lock:{task.uid}"
    service = importutils.import_from_string(task.service)
    with _global_lock_manager.lock(
        lock_key,
        timeout=task.execution_lock_timeout,
        blocking=False,
    ) as locked:
        if locked:
            try:
                if task.is_deleted:
                    # 任务已经标记为删除，无须执行该任务
                    task.set_result(
                        "The task has been marked as deleted and does not need to be executed..."
                    )
                else:
                    # 执行任务
                    result = service(*task.args, **task.kwargs)
                    # 设置任务结果
                    task.set_result(result)
            except Exception as error:
                # 任务处理异常
                # 记录异常并结束回调任务
                # 后续不再重试
                task.set_error(error)
            # 返回任务是否成功
            # 一般不会有人检查该返回值
            return task.success
        else:
            msg = f"callback task {task.uid} locked by another worker..."
            _logger.warning(msg)
            raise RuntimeError(msg)
