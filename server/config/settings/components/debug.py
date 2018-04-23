# -*- coding: utf-8 -*-

INSTALLED_APPS += ['silk',]
MIDDLEWARE += ['silk.middleware.SilkyMiddleware',]
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
