# -*- coding: utf-8 -*-
from django.urls import path

from . import views

urlpatterns = (
    path('', views.home),
    path('payment', views.payment),
    path('authorize', views.authorize),
)
