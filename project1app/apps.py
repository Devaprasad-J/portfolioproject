from django.apps import AppConfig


class Project1AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'project1app'

    def ready(self):
        import project1app.signals
