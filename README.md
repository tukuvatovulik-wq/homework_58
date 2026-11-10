# Домашнее задание №58

Django-проект для работы со списком задач.

## Установка и запуск

```bash
py -m venv venv
venv\Scripts\activate
py -m pip install -r requirements.txt
py manage.py makemigrations
py manage.py migrate
py manage.py loaddata tasks/fixtures/tasks.json
py manage.py runserver
```

Откройте http://127.0.0.1:8000/

## ORM-запросы

Примеры запросов находятся в `tasks/queries.py`.

Откройте Django shell:

```bash
py manage.py shell
```

Затем импортируйте нужные запросы:

```python
from tasks.queries import *
```

## Проверка проекта

```bash
py manage.py check
py manage.py test
```

## Структура

- `tasks/models.py` — модели задач, типов и результатов.
- `tasks/forms.py` — ModelForm задачи.
- `tasks/validators.py` — два пользовательских валидатора.
- `tasks/views.py` — список, просмотр, создание и изменение задач.
- `tasks/queries.py` — ORM-запросы для этапа 2.
- `tasks/fixtures/tasks.json` — демонстрационные данные (18 задач).
