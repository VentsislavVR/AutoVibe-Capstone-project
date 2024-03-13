from django.apps import AppConfig


class CarpostConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'autovibe_project.carpost'
    def ready(self):
        import autovibe_project.carpost.signals