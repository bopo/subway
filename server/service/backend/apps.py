from django.apps import AppConfig


class BackendConfig(AppConfig):
    name = 'service.backend'
    verbose_name = (u'数据服务')

    def ready(self):
        try:
            from .signals import notice
        except ImportError:
            pass
