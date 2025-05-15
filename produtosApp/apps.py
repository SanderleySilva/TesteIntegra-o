from django.apps import AppConfig


class ProdutosappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'produtosApp'

    def ready(self):
        import produtosApp.signals