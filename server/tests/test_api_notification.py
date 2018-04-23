# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model

from .common import BaseAPITestCase


class TestNotificationCase(BaseAPITestCase):
    def setUp(self):
        self.init()

        owenr = get_user_model()()
        owenr.save()

        self._generate_uid_and_token(user=owenr)
        self.client.credentials(HTTP_AUTHORIZATION='Token %s' % self.token)

    def test_notice_fliter(self):
        response = self.client.get("/api/me/notices/")
        self.assertEqual(200, response.status_code)
