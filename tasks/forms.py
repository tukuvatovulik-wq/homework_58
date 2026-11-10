from django import forms

from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "title",
            "short_description",
            "description",
            "status",
            "task_type",
            "result",
        ]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Название задачи"}),
            "short_description": forms.TextInput(
                attrs={"placeholder": "Краткое описание"}
            ),
            "description": forms.Textarea(attrs={"rows": 5}),
            "status": forms.Select(),
            "task_type": forms.Select(),
            "result": forms.Select(),
        }
