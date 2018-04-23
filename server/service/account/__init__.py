# -*- coding: utf-8 -*-
default_app_config = 'service.account.AccountConfig'
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class AccountConfig(AppConfig):
    name = 'service.account'
    verbose_name = _(u'用户管理')
