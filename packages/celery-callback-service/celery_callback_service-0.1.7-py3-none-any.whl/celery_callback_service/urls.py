from django.urls import path
from .views import callback_view
from .constants import CELERY_CALLBACK_SERVICE_VIEW_NAME

urlpatterns = [
    path("callback", callback_view, name=CELERY_CALLBACK_SERVICE_VIEW_NAME),
]
