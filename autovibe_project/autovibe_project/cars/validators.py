from django.utils import timezone


def get_current_year_plus_one():
    return timezone.now().year + 1