import os

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from main.forms import CaptchaPasswordResetForm


class AuthTestCase(TestCase):
    def setUp(self):

        self.user = User.objects.create_user(
            username='refood', email='test@refood-non-profit.org', password='top_secret')

    def test_locked_out_get(self):
        response = self.client.get(reverse('main:locked_out'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/locked_out.html')

    def test_CaptchaPasswordResetForm(self):
        # Recaptcha testing
        # https://github.com/praekelt/django-recaptcha#unit-testing
        os.environ['RECAPTCHA_TESTING'] = 'True'
        form_params = {'g-recaptcha-response': 'PASSED', 'email': 'test@refood-non-profit.org'}
        form = CaptchaPasswordResetForm(form_params)
        self.assertTrue(form.is_valid())

    def test_locked_out_post(self):
        os.environ['RECAPTCHA_TESTING'] = 'True'
        form_params = {'g-recaptcha-response': 'PASSED', 'email': 'test@refood-non-profit.org'}
        response = self.client.post(reverse('main:locked_out'), form_params)
        self.assertEqual(response.status_code, 302)

        response = self.client.post(reverse('main:locked_out'), form_params, REMOTE_ADDR="")
        self.assertContains(response, '<div id="no_ip"', count=1, status_code=200)

    def test_index(self):
        self.client.login(username=self.user.username, password='top_secret')
        response = self.client.get(reverse('main:index'))

        self.assertTemplateUsed(response, 'main/index.html')
        self.assertEqual(response.status_code, 200)