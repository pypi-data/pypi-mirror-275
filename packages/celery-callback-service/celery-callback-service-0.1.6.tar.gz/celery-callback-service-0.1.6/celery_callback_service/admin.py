from django.contrib import admin
from django.contrib.auth import get_permission_codename
from django_admin_daterange_listfilter.filters import DateRangeFilter
from django_model_helper.actions import set_deleted_for_selected
from django_model_helper.actions import set_undeleted_for_selected
from django_model_helper.admin import WithDeletedStatusFieldsAdmin
from .models import Task
from .actions import restart_celery_callback_service


class TaskAdmin(
    WithDeletedStatusFieldsAdmin,
):
    list_display = [
        "uid",
        "service",
        "deleted_display",
        "success",
        "add_time",
        "result_time",
    ]
    list_filter = [
        "success",
        "service",
        "deleted",
        ("add_time", DateRangeFilter),
        ("mod_time", DateRangeFilter),
        ("result_time", DateRangeFilter),
    ]
    search_fields = [
        "uid",
        "celery_task_id",
    ]
    fieldsets = (
        (
            "基础信息",
            {
                "fields": [
                    "uid",
                    "service",
                    "args_raw",
                    "kwargs_raw",
                    "deleted",
                ]
            },
        ),
        (
            "Celery任务信息",
            {
                "fields": [
                    "celery_task_id",
                    "celery_task_start_time",
                ]
            },
        ),
        (
            "执行结果信息",
            {
                "fields": [
                    "success",
                    "result_data",
                    "error_data",
                    "result_time",
                ]
            },
        ),
        (
            "时间信息",
            {
                "fields": [
                    "add_time",
                    "mod_time",
                    "deleted_time",
                ]
            },
        ),
    )
    actions = [
        restart_celery_callback_service,
        set_deleted_for_selected,
        set_undeleted_for_selected,
    ]

    def has_restart_celery_callback_service_permission(self, request):
        opts = self.opts
        codename = get_permission_codename("publish", opts)
        return request.user.has_perm("%s.%s" % (opts.app_label, codename))


admin.site.register(Task, TaskAdmin)
