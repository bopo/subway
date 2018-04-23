# -*- coding: utf-8 -*-
from django.urls import path

from .views import RegisterView, VerifyMobileView

urlpatterns = (
    path('', RegisterView.as_view(), name='rest_register'),
    path('verify_mobile/', VerifyMobileView.as_view(), name='rest_verify_mobile'),
)
