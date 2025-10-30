from django.apps import AppConfig


class ModuleConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core.apps.dashboard"

    def ready(self):
        import core.apps.dashboard.signals.payme.payme
        import core.apps.dashboard.signals.click.click
