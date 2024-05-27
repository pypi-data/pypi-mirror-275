from django.contrib import admin


@admin.action(
    description="重新向Celery推送所选的 %(verbose_name)s",
    permissions=["restart_celery_callback_service"],
)
def restart_celery_callback_service(modeladmin, request, queryset):
    restarted = 0
    for item in queryset.all():
        item.clean_result(save=False)
        item.start_celery_callback_service(save=False)
        item.save()
        restarted += 1
    modeladmin.message_user(
        request,
        f"重新向Celery推送了所选的 {restarted}个 {modeladmin.model._meta.verbose_name}。",
    )
