"""
Примеры ORM-запросов для домашнего задания №58.

Запуск в Django shell:
    py manage.py shell
    from tasks.queries import *
"""

from datetime import timedelta

from django.db.models import Count, F, Q
from django.utils import timezone

from .models import Task


# 1. Закрытые задачи, обновлённые за последний месяц.
now = timezone.now()
month_ago = now - timedelta(days=30)

closed_tasks_last_month = Task.objects.filter(
    status=Task.Status.CLOSED,
    updated_at__range=(month_ago, now),
)


# 2. Задачи по двум статусам, двум типам и двум результатам.
# Названия типов и результатов существуют в фикстурах.
tasks_by_status_type_result = Task.objects.filter(
    status__in=[Task.Status.NEW, Task.Status.IN_PROGRESS],
    task_type__name__in=["Баг", "Улучшение"],
    result__name__in=["Исправлено", "Ожидает проверки"],
)


# 3. Не закрытые задачи: в названии есть «ошибка» ИЛИ тип задачи — «Баг».
not_closed_error_or_bug = Task.objects.filter(
    ~Q(status=Task.Status.CLOSED)
).filter(
    Q(title__icontains="ошибка") | Q(task_type__name="Баг")
)


# Бонус 1. Только ID, название задачи, название типа и название результата.
tasks_short_values = Task.objects.values(
    "id",
    "title",
    task_type_name=F("task_type__name"),
    result_name=F("result__name"),
)


# Бонус 2. Задачи с точным совпадением краткого описания.
tasks_exact_short_description = Task.objects.filter(
    short_description="Необходимо исправить найденную ошибку."
)


# Бонус 3. Количество задач каждого типа.
tasks_count_by_type = Task.objects.values(
    "task_type__name"
).annotate(
    tasks_count=Count("id")
).order_by("task_type__name")
