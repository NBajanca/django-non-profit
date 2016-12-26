from django.contrib.auth.models import User
from django.test import TestCase

from volunteers.models import Volunteer


class VolunteerTestCase(TestCase):
    def setUp(self):

        self.user = User.objects.create_user(
            username='refood', email='test@refood-non-profit.org', password='top_secret')
        Volunteer.objects.create(user=self.user, car_availability=True)

    def test_Volunteer_str(self):
        self.assertEqual(str(self.user.volunteer), self.user.get_username())

        self.user.first_name = 'Re'
        self.user.last_name = 'Food'
        self.user.save()

        self.assertEqual(str(self.user.volunteer), self.user.get_full_name())
