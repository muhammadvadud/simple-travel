from django.apps import AppConfig


class ModuleConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core.apps.tickets"
    label = "tickets"

    def ready(self):
        import core.apps.tickets.signals
        import core.apps.dashboard.signals.payme.payme
        import core.apps.dashboard.signals.click.click
