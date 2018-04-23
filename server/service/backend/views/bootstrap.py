# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ..models.bootstrap import Feedback, Version
from ..serializers.bootstrap import FeedbackSerializers, VersionSerializer


class VersionViewSet(viewsets.GenericViewSet):
    '''
    手机应用版本更新接口
    '''
    serializer_class = VersionSerializer

    def list(self, request, *args, **kwargs):
        platform = request.GET.get('platform')
        instance = Version.objects.filter(platform=platform).order_by('-id').first()
        serializer = self.get_serializer(instance)

        return Response(serializer.data)


class FeedbackViewSet(viewsets.ModelViewSet):
    '''
    意见反馈接口
    '''
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializers
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.queryset.filter(owner=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

# class BannerViewSet(viewsets.ReadOnlyModelViewSet):
#     '''
#     广告管理接口
#     '''
#     queryset = Banner.objects.all()
#     serializer_class = BannerSerializers
#     # permission_classes = (IsAuthenticated,)
