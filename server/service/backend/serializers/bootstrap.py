# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers

from ..models.bootstrap import Feedback, Version


class VersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Version
        fields = ('version', 'depends', 'install', 'sha1sum', 'channel', 'constraint', 'summary', 'platform')


class FeedbackSerializers(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        # read_only_fields = ("level", 'credit', 'avatar')
        # exclude = ('owner',)
        fields = ('title', 'phone', 'content', 'storage')
