# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# -*- coding: utf-8 -*-
from split_settings.tools import optional, include

include(
    'components/base.py',
    'components/apps.py',
    'components/rest.py',
    'components/suit.py',

    'components/static.py',
    'components/celery.py',

    'components/cache.py',
    'components/thumb.py',
    'components/store.py',
)

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '..', 'db.sqlite3'),
    }
}
DEBUG = False
