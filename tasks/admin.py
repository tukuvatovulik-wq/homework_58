from django.contrib import admin

from .models import Task, TaskResult, TaskType


@admin.register(TaskType)
class TaskTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(TaskResult)
class TaskResultAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "status", "task_type", "result", "updated_at")
    list_filter = ("status", "task_type", "result")
    search_fields = ("title", "short_description")
