# -*- coding: utf-8 -*-

AWS_S3_SIGNATURE_VERSION = env('DJANGO_MINIO_VERSION', default='s3v4')
AWS_S3_ENDPOINT_URL      = env('DJANGO_MINIO_ENCRYPTION', default='http://127.0.0.1:9000')
AWS_S3_REGION_NAME       = env('DJANGO_MINIO_REGION', default='us-east-1')
AWS_S3_ENCRYPTION        = env('DJANGO_MINIO_ENCRYPTION', default=False)

AWS_ACCESS_KEY_ID        = env('DJANGO_MINIO_ACCESSKEY', default='O21TSRP1HLRNR84YU0QV')
AWS_SECRET_ACCESS_KEY    = env('DJANGO_MINIO_SECRETKEY', default='+VPu5glwaD8fXLJKJ8kLQOZDC/nEfKKvXuJXh2we')
AWS_STORAGE_BUCKET_NAME  = env('DJANGO_MINIO_BUCKET', default='storage')

DEFAULT_FILE_STORAGE     = 'storages.backends.s3boto3.S3Boto3Storage'
