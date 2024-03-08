from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'autovibe_project.accounts'

    def ready(self):
        import autovibe_project.accounts.signals
