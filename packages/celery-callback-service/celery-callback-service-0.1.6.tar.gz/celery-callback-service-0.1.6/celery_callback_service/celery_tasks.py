# 注意：
# 在`celery-callback-worker`（即celery回调任务执行器）中，`celery_callback_service_cipher`应该使用私钥进行初始化。
# 在`celery-callback-service`的客户端侧，`celery_callback_service_cipher`应该使用公钥进行初始化。
# 如果在一个程序即当服务端又当客户端，则使用私钥进行初始化。


import time
import datetime
import requests

from celery.app import app_or_default
from celery.utils.log import get_logger
from celery_debug.utils import use_different_queue


__all__ = [
    "app",
    "celery_callback_service_execute",
    "celery_callback_service_execute_start",
]

app = app_or_default()
_logger = get_logger(__name__)


CELERY_CALLBACK_RETRY_COUNTDOWN_STEP = getattr(
    app,
    "celery_callback_retry_countdown_step",
    5,
)
CELERY_CALLBACK_RETRY_COUNTDOWN_MAX = getattr(
    app,
    "celery_callback_retry_countdown_max",
    300,
)
CELERY_CALLBACK_MAX_RETRIES = getattr(
    app,
    "celery_callback_max_retries",
    2048,
)


@app.task(name="celery_callback_service.execute", bind=True)
def celery_callback_service_execute(task, data):
    """执行一个celery回调任务。"""
    # 参数解密
    data = app.conf.celery_callback_service_cipher.decrypt(data)
    # 获取回调url
    url = data["url"]
    del data["url"]
    # 获取回调apikey
    apikey = data["apikey"]
    del data["apikey"]
    # 获取回调timeout
    timeout = 60
    if "timeout" in data:
        timeout = data["timeout"]
        del data["timeout"]
    headers = {
        "Authorization": "Bearer " + apikey,
    }

    _logger.debug(
        "celery_callback_service.execute calling back: url=%s, json=%s, headers=%s, timeout=%s",
        url,
        data,
        headers,
        timeout,
    )
    error = None
    try:
        response = requests.post(
            url,
            json=data,
            headers=headers,
            timeout=timeout,
        )
        if response.status_code == 200:
            # 回调成功，正常返回并结束任务
            return response.content
        else:
            # 回调失败，纳入重试
            # 一般为未捕获的接口异常
            error = RuntimeError("callback response code is NOT 200...")
    except Exception as err:
        # 回调失败，纳入重试
        # 一般为网络异常
        error = err

    print(error)
    # 纳入重试
    task.retry(
        error=error,
        countdown=min(
            CELERY_CALLBACK_RETRY_COUNTDOWN_STEP * task.request.retries,
            CELERY_CALLBACK_RETRY_COUNTDOWN_MAX,
        ),
        max_retries=CELERY_CALLBACK_MAX_RETRIES,
    )


# 必须要在`celery_callback_service_execute`定义之后
use_different_queue(app)


def _get_execute_time(delay_seconds):
    return datetime.datetime.utcfromtimestamp(time.time() + delay_seconds)


def celery_callback_service_execute_start(task, cipher=None, delay_seconds=5):
    """启动一个celery回调任务。"""
    cipher = cipher or app.conf.celery_callback_service_cipher
    data = cipher.encrypt(task)
    return celery_callback_service_execute.apply_async(
        args=[data],
        eta=_get_execute_time(delay_seconds),
    )
