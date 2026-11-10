from django.db import models

from .validators import (
    validate_short_description_min_length,
    validate_title_min_length,
)


class TaskType(models.Model):
    name = models.CharField("Название типа", max_length=100, unique=True)

    class Meta:
        verbose_name = "Тип задачи"
        verbose_name_plural = "Типы задач"
        ordering = ["name"]

    def __str__(self):
        return self.name


class TaskResult(models.Model):
    name = models.CharField("Название результата", max_length=100, unique=True)

    class Meta:
        verbose_name = "Результат"
        verbose_name_plural = "Результаты"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Task(models.Model):
    class Status(models.TextChoices):
        NEW = "new", "Новая"
        IN_PROGRESS = "in_progress", "В работе"
        CLOSED = "closed", "Закрыта"

    title = models.CharField(
        "Название задачи",
        max_length=150,
        validators=[validate_title_min_length],
    )
    short_description = models.CharField(
        "Краткое описание",
        max_length=250,
        validators=[validate_short_description_min_length],
    )
    description = models.TextField("Описание", blank=True)
    status = models.CharField(
        "Статус",
        max_length=20,
        choices=Status.choices,
        default=Status.NEW,
    )
    task_type = models.ForeignKey(
        TaskType,
        on_delete=models.PROTECT,
        related_name="tasks",
        verbose_name="Тип задачи",
    )
    result = models.ForeignKey(
        TaskResult,
        on_delete=models.PROTECT,
        related_name="tasks",
        verbose_name="Результат",
    )
    created_at = models.DateTimeField("Создана", auto_now_add=True)
    updated_at = models.DateTimeField("Последнее обновление", auto_now=True)

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
        ordering = ["-updated_at"]

    def __str__(self):
        return self.title
