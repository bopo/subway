# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r'notification', NotificationViewSet, 'me-notices')

urlpatterns = (
    path('', include(router.urls)),
    path('profile/', ProfileViewSet.as_view(), name='me-profile'),
    path('profile/avatar/', AvatarViewSet.as_view(), name='profile-avatar'),
)
