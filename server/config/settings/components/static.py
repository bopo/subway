# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

# try:
#     from .base import *
# except ImportError as e:
#     raise e

MEDIA_URL = env('DJANGO_MEDIA_URL', default='/media/')
STATIC_URL = env('DJANGO_STATIC_URL', default='/static/')

STATIC_ROOT = str(ROOT_DIR.path('assets/static'))

THUMB_ROOT = str(ROOT_DIR.path('assets/media/thumb'))
MEDIA_ROOT = str(ROOT_DIR.path('assets/media'))

ADMIN_MEDIA_PREFIX = MEDIA_URL

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
