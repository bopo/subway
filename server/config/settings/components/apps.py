# -*- coding: utf-8 -*-
import os

INSTALLED_APPS += (
    'service.frontend',
    'service.frontend.dashboard',

    'service.account',
    'service.backend',

    'service.passport',
    'service.passport.registration',
    'service.wechat',

    'django_extensions',
    'import_export',
    'reversion',
    'haystack',
    'imagekit',
    'filters',
)
