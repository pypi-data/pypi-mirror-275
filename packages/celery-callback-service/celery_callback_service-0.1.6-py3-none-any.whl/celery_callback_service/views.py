from django_apis.views import get_apiview
from django_apis.views import get_json_payload
from django_apis.views import http_bearer_auth_protect
from django_apis.exceptions import InputValidationError

from .forms import CallbackInput
from .services import celery_callback_service
from .settings import CELERY_CALLBACK_SERVICE_APIKEYS

apiview = get_apiview()


@apiview(methods="post")
def callback_view(request):
    """回调任务调度接口。"""
    http_bearer_auth_protect(request, apikeys=CELERY_CALLBACK_SERVICE_APIKEYS)
    payload = get_json_payload(request)
    form = CallbackInput(payload)
    if not form.is_valid():
        raise InputValidationError(form)
    uid = form.cleaned_data["uid"]
    return celery_callback_service(uid)
