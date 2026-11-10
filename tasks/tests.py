from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse

from .forms import TaskForm
from .models import Task, TaskResult, TaskType


class TaskProjectTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.task_type = TaskType.objects.create(name="Баг")
        cls.result = TaskResult.objects.create(name="Исправлено")
        cls.task = Task.objects.create(
            title="Проверить форму",
            short_description="Проверка корректной работы формы.",
            status=Task.Status.NEW,
            task_type=cls.task_type,
            result=cls.result,
        )

    def test_title_validator_rejects_short_title(self):
        form = TaskForm(data={
            "title": "Тест",
            "short_description": "Достаточно длинное описание.",
            "description": "",
            "status": Task.Status.NEW,
            "task_type": self.task_type.pk,
            "result": self.result.pk,
        })
        self.assertFalse(form.is_valid())
        self.assertIn("title", form.errors)

    def test_short_description_validator_rejects_short_text(self):
        form = TaskForm(data={
            "title": "Проверить задачу",
            "short_description": "Коротко",
            "description": "",
            "status": Task.Status.NEW,
            "task_type": self.task_type.pk,
            "result": self.result.pk,
        })
        self.assertFalse(form.is_valid())
        self.assertIn("short_description", form.errors)

    def test_task_list_page(self):
        response = self.client.get(reverse("tasks:list"))
        self.assertEqual(response.status_code, 200)

    def test_task_create_page(self):
        response = self.client.get(reverse("tasks:create"))
        self.assertEqual(response.status_code, 200)

    def test_task_update_page(self):
        response = self.client.get(
            reverse("tasks:update", kwargs={"pk": self.task.pk})
        )
        self.assertEqual(response.status_code, 200)

    def test_task_create_post(self):
        response = self.client.post(
            reverse("tasks:create"),
            {
                "title": "Создать новую задачу",
                "short_description": "Описание новой задачи для проверки.",
                "description": "",
                "status": Task.Status.NEW,
                "task_type": self.task_type.pk,
                "result": self.result.pk,
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), 2)

    def test_task_update_post(self):
        response = self.client.post(
            reverse("tasks:update", kwargs={"pk": self.task.pk}),
            {
                "title": "Обновлённое название",
                "short_description": "Обновлённое краткое описание.",
                "description": "",
                "status": Task.Status.IN_PROGRESS,
                "task_type": self.task_type.pk,
                "result": self.result.pk,
            },
        )
        self.assertEqual(response.status_code, 302)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, "Обновлённое название")
