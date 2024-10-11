from django.apps import AppConfig


class SignalsAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Signals_app'

    def ready(self):
        from . import signal