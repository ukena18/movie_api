from django.apps import AppConfig


class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base'

    # that is for running our signals everytime
    # we save something to the database
    def ready(self):
        # run signal.py everytime we play with db
        import base.signals