from django.test import TestCase
from eventex.subscriptions.models import Subscription
from django.shortcuts import resolve_url as r


class SubscriptionDetailGet(TestCase):
    def setUp(self):
        self.obj = Subscription.objects.create(
            name='Henrique Bastos',
            cpf='12345678901',
            email='teste@lcotta.com',
            phone='21-996186180'
        )
        self.resp = self.client.get(r('subscriptions:detail', self.obj.hashid))


    def test_get(self):
        self.assertEqual(200, self.resp.status_code)


    def test_template(self):
        self.assertTemplateUsed(self.resp,
                                'subscriptions/subscription_detail.html')


    def test_context(self):
        subscription = self.resp.context['subscription']
        self.assertIsInstance(subscription, Subscription)


    def test_html(self):
        contents = (self.obj.name, self.obj.cpf,
                    self.obj.email, self.obj.phone)

        with self.subTest():
            for expected in contents:
                self.assertContains(self.resp, expected)


class SubcriptionDetailNotFound(TestCase):
    def test_not_found(self):
        resp = self.client.get(r('subscriptions:detail', 0))
        self.assertEqual(404, resp.status_code)


