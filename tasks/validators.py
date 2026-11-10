from django.core.exceptions import ValidationError


def validate_title_min_length(value):
    """Название задачи должно содержать не менее 5 символов."""
    if len(value.strip()) < 5:
        raise ValidationError(
            "Название задачи должно содержать не менее 5 символов.",
            code="title_too_short",
        )


def validate_short_description_min_length(value):
    """Краткое описание должно содержать не менее 10 символов."""
    if len(value.strip()) < 10:
        raise ValidationError(
            "Краткое описание должно содержать не менее 10 символов.",
            code="description_too_short",
        )
