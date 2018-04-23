# -*- coding: utf-8 -*-

from datetime import timedelta

# try:
#     from .base import *
# except ImportError as e:
#     raise e

INSTALLED_APPS += (
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_swagger',
)

REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'service.backend.exception.custom_exception_handler',
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.NamespaceVersioning',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        # 'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework_msgpack.renderers.MessagePackRenderer',
        # 'rest_framework_xml.renderers.XMLRenderer',
        # 'rest_framework_yaml.renderers.YAMLRenderer',
    ),
    'DEFAULT_FILTER_BACKENDS': [
        # 'url_filter.integrations.drf.DjangoFilterBackend',
        # 'django_filters.rest_framework.DjangoFilterBackend',
    ],

    # 'DEFAULT_FILTER_BACKENDS': (
    #     'rest_framework_filters.backends.DjangoFilterBackend',
    # ),
    # 'DEFAULT_PARSER_CLASSES': (
    #     'rest_framework.parsers.JSONParser',
    #     'rest_framework_xml.parsers.XMLParser',
    #     'rest_framework_msgpack.parsers.MessagePackParser',
    #     'rest_framework_yaml.parsers.YAMLParser',
    # ),
    # 'DEFAULT_THROTTLE_RATES': {
    #     'anon': '100/day',
    #     'user': '1000/day'
    # },
    'PAGE_SIZE': 20,
    'DATETIME_FORMAT': '%Y-%m-%d %H:%M:%S',

}

if DEBUG:
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] += (
        'rest_framework.renderers.BrowsableAPIRenderer'
    )

REST_AUTH_SERIALIZERS = {
    # 'LOGIN_SERIALIZER': 'path.to.custom.LoginSerializer',
    # 'TOKEN_SERIALIZER': 'path.to.custom.TokenSerializer',
    # 'USER_DETAILS_SERIALIZER': 'service.consumer.serializers.AccountDetailsSerializer',
}

REST_FRAMEWORK_EXTENSIONS = {
    'DEFAULT_USE_CACHE': 'default'
}

# from rest_framework.versioning import URLPathVersioning
CORS_ORIGIN_ALLOW_ALL = True

ACCOUNT_EMAIL_VERIFICATION = None
OLD_PASSWORD_FIELD_ENABLED = True


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}
