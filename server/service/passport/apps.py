# -*- coding: utf-8 -*-
from django.apps import AppConfig


class PassportConfig(AppConfig):
    name = 'service.passport'
    verbose_name = u'认证管理'

    def ready(self):
        pass
