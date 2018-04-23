# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views.bootstrap import FeedbackViewSet, VersionViewSet

router = DefaultRouter()
router.register('feedback', FeedbackViewSet, base_name='feedback')
router.register('version', VersionViewSet, base_name='version')

urlpatterns = (
    path('', include(router.urls)),
    path('me/', include('service.account.urls')),
    # path('im/', include('service.message.urls')),

    path('auth/', include('service.passport.urls')),
    path('rest/', include('rest_framework.urls', namespace='rest_framework')),
)
