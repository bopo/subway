# -*- coding: utf-8 -*-

from rest_framework import serializers

from .models import Profile, Notification


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("name", 'nick', 'avatar')
        # read_only_fields = ("level", 'credit', 'avatar')
        # exclude = ('owner',)


class AvatarSerializer(ProfileSerializer):
    class Meta:
        model = Profile
        fields = ('avatar')
        # read_only_fields = ("level", 'credit', 'avatar')
        # exclude = ('owner',)


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ('subject', 'content')
