try:
    from .base import *
except Exception as e:
    raise e

DEBUG = True
SILK_ENABLE = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '..', 'test.sqlite3'),
    }
}