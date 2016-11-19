from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from volunteers.models import Volunteer, VolunteerComplementaryContact


class VolunteerTestCase(TestCase):
    def setUp(self):

        self.user = User.objects.create_user(
            username='refood', email='test@refood-non-profit.org', password='top_secret')

        volunteer = Volunteer.objects.create(user=self.user, mobile_phone='+351999999999')

        self.volunteer_complementary_contact = \
            VolunteerComplementaryContact.objects.create(volunteer=volunteer, first_name='Cascais', last_name='CPR',
                                                         contact_type=VolunteerComplementaryContact.ICE)

    def test_Volunteer_str(self):
        self.assertEqual(str(self.user.volunteer), self.user.get_username())

        self.user.first_name = 'Re'
        self.user.last_name = 'Food'
        self.user.save()

        self.assertEqual(str(self.user.volunteer), self.user.get_full_name())

    def test_VolunteerComplementaryContact_str(self):
        self.assertEqual(str(self.user.volunteer.volunteer_complementary_contact_list.first()),
                         self.user.get_username() + ' - ' + self.volunteer_complementary_contact.first_name + ' ' +
                         self.volunteer_complementary_contact.last_name)





