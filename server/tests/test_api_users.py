# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model

from .common import BaseAPITestCase


class APITestUser(BaseAPITestCase):
    def setUp(self):
        self.init()

        self.owenr = get_user_model()(username='owenr')
        self.owenr.save()

        self.invite = get_user_model()(username='invite')
        self.invite.save()

        self._generate_uid_and_token(user=self.owenr)
        self.client.credentials(HTTP_AUTHORIZATION='Token %s' % self.token)

    def test_user_invite(self):
        data = {'black': '1', 'alias': '1', 'hide': '1'}
        resp = self.client.post('/api/users/%d/invite/' % self.invite.pk, data=data)
        self.assertEquals(resp.status_code, 201, msg=resp)

    def test_user_report(self):
        resp = self.client.post('/api/users/%d/report/' % self.invite.pk, {'content': 'content'})
        self.assertEquals(resp.status_code, 201, msg=resp)
