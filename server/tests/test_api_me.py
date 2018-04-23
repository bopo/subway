# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model

from .common import BaseAPITestCase


class APITestMe(BaseAPITestCase):
    def setUp(self):
        self.init()

        owenr = get_user_model()()
        owenr.save()

        self._generate_uid_and_token(user=owenr)
        self.client.credentials(HTTP_AUTHORIZATION='Token %s' % self.token)

    def test_get_profile(self):
        response = self.client.get('/api/me/profile/')
        self.assertEqual(response.status_code, 200, msg=response.conent)

    def test_put_profile(self):
        payload = {
            "nick": "你好",
            "gender": "male",
            "birthday": "2017-11-29",
            "friend_verify": True,
            "mobile_verify": True,
            "name_public": True,
            "avatar": open('assets/media/avatar/default.jpg', 'rb')
        }

        response = self.client.put('/api/me/profile/', payload)
        self.assertEqual(response.status_code, 200, msg=response)

    def test_get_avatar(self):
        response = self.client.get('/api/me/profile/avatar/')
        self.assertEqual(response.status_code, 200, msg=response)

    def test_put_avatar(self):
        payload = {"avatar": open('assets/media/avatar/default.jpg', 'rb')}
        response = self.client.put('/api/me/profile/avatar/', payload)
        self.assertEqual(response.status_code, 200, msg=response)

    def test_get_nick(self):
        response = self.client.get('/api/me/profile/nick/')
        self.assertEqual(response.status_code, 200, msg=response)

    def test_put_nick(self):
        payload = {"nick": "张三"}
        response = self.client.put('/api/me/profile/nick/', payload)
        self.assertEqual(response.status_code, 200, msg=response)
