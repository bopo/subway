# -*- coding: utf-8 -*-

# 融云 API 参数
RONGCLOUD_APPKEY = env('RONGCLOUD_APPKEY', default='')
RONGCLOUD_SECRET = env('RONGCLOUD_SECRET', default='')

# 极光 API 参数
JPUSH_APPKEY = env('DJANGO_JPUSH_APPKEY', default='')
JPUSH_SECRET = env('DJANGO_JPUSH_SECRET', default='')
JPUSH_OPTION = {
    "apns_production": env('DJANGO_JPUSH_PRODUCTION', default=False),
    "time_to_live": 86400, 
    "sendno": 12345, 
}

# 微信公众号 API 参数
WECHAT_APPKEY = env('DJANGO_WECHAT_APPKEY', default='')
WECHAT_SECRET = env('DJANGO_WECHAT_SECRET', default='')
WECHAT_OPTION = {}

# 微信小程序 API 参数
WEAPPS_APPKEY = env('DJANGO_WEAPPS_APPKEY', default='')
WEAPPS_SECRET = env('DJANGO_WEAPPS_SECRET', default='')
WEAPPS_OPTION = {}