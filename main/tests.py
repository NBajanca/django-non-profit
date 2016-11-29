import os
import json

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from main.forms import CaptchaPasswordResetForm
from volunteers.models import Volunteer


class AuthTestCase(TestCase):
    def setUp(self):

        self.user = User.objects.create_user(
            username='refood', email='test@refood-non-profit.org', password='top_secret')

    def test_locked_out_get(self):
        response = self.client.get(reverse('main:locked_out'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'auth/locked_out.html')

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

    def test_profile(self):
        self.client.login(username=self.user.username, password='top_secret')
        response = self.client.get(reverse('main:profile', args=[self.user.pk]))

        self.assertTemplateUsed(response, 'main/profile.html')
        self.assertContains(response, str(self.user.email) , count=1, status_code=200)

    def test_volunteer_profile(self):
        Volunteer.objects.create(user=self.user, mobile_phone='+351999999999')

        self.client.login(username=self.user.username, password='top_secret')
        response = self.client.get(reverse('main:profile', args=[self.user.pk]))

        self.assertTemplateUsed(response, 'main/profile.html')
        self.assertContains(response, str(self.user.volunteer.mobile_phone), count=1, status_code=200)


    def test_edit_profile(self):
        self.client.login(username=self.user.username, password='top_secret')
        response = self.client.get(reverse('main:edit_profile', args=[self.user.pk]))

        self.assertTemplateUsed(response, 'main/edit_profile.html')
        self.assertContains(response, str(self.user.username) , count=1, status_code=200)

        response = self.client.get(reverse('main:edit_profile', args=[self.user.pk + 1]))
        self.assertEqual(response.status_code, 404)

    def test_edit_profile_user(self):
        self.client.login(username=self.user.username, password='top_secret')

        data = {'username': 'refood','first_name': 'Refood','last_name': 'Cascais CPR'}
        response = self.client.post(reverse('main:edit_profile_user', args=[self.user.pk]), data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.get(username='refood').first_name, 'Refood')

        data = {'first_name': 'Refood', 'last_name': 'Cascais CPR'}
        response = self.client.post(reverse('main:edit_profile_user', args=[self.user.pk]), data)
        self.assertEqual(response.status_code, 400)

        response = self.client.get(reverse('main:edit_profile_user', args=[self.user.pk +1]))
        self.assertEqual(response.status_code, 404)

    def test_edit_profile_password(self):
        self.client.login(username=self.user.username, password='top_secret')

        data = {'old_password': 'top_secret', 'new_password1': 'top_secret2', 'new_password2': 'top_secret2'}
        response = self.client.post(reverse('main:edit_profile_password', args=[self.user.pk]), data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(self.client.login(username=self.user.username, password='top_secret2'))

        data = {'old_password': 'top_secret', 'new_password1': 'top_secret2', 'new_password2': 'top_secret2'}
        response = self.client.post(reverse('main:edit_profile_password', args=[self.user.pk]), data)
        self.assertEqual(response.status_code, 400)

        response = self.client.get(reverse('main:edit_profile_password', args=[self.user.pk +1]))
        self.assertEqual(response.status_code, 404)
