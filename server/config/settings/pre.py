# -*- coding: utf-8 -*-
from split_settings.tools import optional, include
from psycopg2.extensions import ISOLATION_LEVEL_SERIALIZABLE

include(
    'components/base.py',
    'components/apps.py',
    'components/rest.py',
    'components/suit.py',
    'components/logs.py',

    'components/static.py',
    'components/celery.py',
    'components/search.py',

    'components/email.py',
    'components/cache.py',
    'components/thumb.py',
    'components/store.py',
)

DEBUG = env('DJANGO_DEBUG', default=False)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('POSTGRES_NAME', default='demo'),
        'USER': env('POSTGRES_USER', default='demo'),
        'PASSWORD': env('POSTGRES_PASS', default='demo'),
        'HOST': env('POSTGRES_HOST', default='localhost'),
        'PORT': env('POSTGRES_PORT', default='5432'),
        'OPTIONS': {
            'isolation_level': ISOLATION_LEVEL_SERIALIZABLE,
            'client_encoding': 'UTF8',
        },
        'timezone': 'UTC',
    }
}