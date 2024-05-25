# celery-callback-service

基于celery的回调服务。业务系统创建celery回调任务，celery-callback-worker执行回调任务，业务系统在回调任务中处理异步任务。


## 使用方法

###  启动`celery-callback-worker`（celery worker）

*celeryconfig.py*

```python
worker_concurrency = 10
worker_pool = "threads"
broker_url = "redis://redis/0"
result_backend = "redis://redis/1"
accept_content = ["application/json"]
task_serializer = "json"
result_accept_content = ["application/json"]
result_serializer = "json"
timezone = "Asia/Shanghai"
broker_connection_retry_on_startup = True
task_track_started = True
task_acks_late = True
task_acks_on_failure_or_timeout = True
task_reject_on_worker_lost = True
# 额外新增的配置项
# 配置后所有任务都使用不同的队列
use_different_queue = True

from hybrid_cipher import HybridCipher

celery_callback_service_cipher_key = """
-----BEGIN RSA PRIVATE KEY-----
xxxxxx 请自行生成rsa证书
xxxxxx from Crypto.PublicKey import RSA
xxxxxx sk = RSA.generate(1024)
xxxxxx print(sk.export_key().decode())
xxxxxx 
xxxxxx celery-callback-worker侧使用私钥
xxxxxx celery-callback-service业务侧使用公钥
-----END RSA PRIVATE KEY-----
""".strip()
celery_callback_service_cipher = HybridCipher(celery_callback_service_cipher_key)
```

*start.sh*
```
#!/bin/bash
celery -l celery_callback_service.celery_tasks:app worker -l DEBUG
```

执行`./start.sh`启动`celery-callback-worker`。

### 业务程序中引入`celery-callback-service`

*celeryconfig.py*

```python
# 与celery-callback-worker中的celeryconfig.py保持一致
# 这是celery-callback-worker中的私钥需要更新为相应的公钥
```

*pro/settings.py*

```python
INSTALLED_APPS = [
    ...
    "django_admin_daterange_listfilter",
    "celery_callback_service",
    ...
]

# 这里用于设置回调接口访问的APIKEYS
# 允许多个，请定期更换
CELERY_CALLBACK_SERVICE_APIKEYS = [
    "yEcU2IrtVGslTgw6JmkoTo4Trkplnyg8",
    "kBhZB8yKKFmXoAzFHP7HVembYsAeOyBk",
]
# 这里的服务地址必须`celery-callback-worker`能够访问的地址
CELERY_CALLBACK_SERVICE_ADDRESS = "http://127.0.0.1:8000"
```

*初始化`celery-callback-service`相关数据表*

```shell
python manage.py migrate celery_callback_service
```

`app/tasks.py`

```python
def task1(arg1, arg2):
   pass

task1.execution_lock_timeout = 60 # 设置回调任务的锁定时间。默认60秒。
task1.delay_seconds = 5 # 设置n秒后再回调。默认是5秒后再回调。主要是避免在业务接口中创建的Task还没有commit到数据库，导致回调时Task任务不可见。
```

*注意：task1等回调函数，必须全局可见。*


`app/services.py`

```python
from celery_callback_service.client import start_callback_service
from .tasks import task1

def service_func1(*args, **kwargs):
    ...
    start_callback_service(task1, arg1, arg2...)
    ...
```


## 配置项

### 业务侧`settings.py`额外配置项

- CELERY_CALLBACK_SERVICE_APIKEYS
    - 不设置的话，优先继承`DJANGO_APIS_APIKEYS`配置项的值
    - 如果`DJANGO_APIS_APIKEYS`也没有设置的话，则自动生成随机授权码，并打印输出。
- CELERY_CALLBACK_SERVICE_ADDRESS
    - 如果不设置，则在启动时告警。不设置的话，是没有办法正常回调的。

### 业务侧`celeryconfig.py`额外配置项

- celery_callback_service_cipher: 无默认值，必须的配置项
- celery_callback_retry_countdown_step: 5
- celery_callback_retry_countdown_max: 300
- celery_callback_max_retries: 2048


## 回调异常的说明

- 如果回调执行过程中出现程序逻辑异常，则会结束该回调任务，并把错误信息记录在记录表中。
- 如果回调执行过程中出现网络异常、网关异常等HTTP状态码非200的情况，则会将任务纳入重试。
    - 重试延迟规则是：5秒（可配置） * 重试次数，最大延迟300秒（可配置）。

## 版本记录

### v0.1.6

- 版本首发。
