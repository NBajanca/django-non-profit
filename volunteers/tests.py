from django.contrib.auth.models import User
from django.test import RequestFactory
from django.test import TestCase

from volunteers.models import Volunteer, Task, Shift, Preference, VolunteerShift, VolunteerUnavailability, \
    VolunteerPresence
from volunteers.views import index


class VolunteerTestCase(TestCase):
    def setUp(self):

        self.user = User.objects.create_user(username='refood', email='test@refood-non-profit.org',
                                             password='top_secret')
        Volunteer.objects.create(user=self.user, car_availability=True)

        self.task = Task.objects.create(name='Distribuição', slug='distribuicao', place='BO', time_beginning='19:30:00',
                                        time_ending='21:30:00', min_volunteers='4', max_volunteers='6')
        self.shift = Shift.objects.create(task=self.task, day_of_the_week='1')
        self.preference = Preference.objects.create(volunteer=self.user.volunteer, shift=self.shift, priority=1)
        self.volunteer_shift = VolunteerShift.objects.create(volunteer=self.user.volunteer, shift=self.shift,
                                                             frequency='W')
        self.volunteer_unavailability = VolunteerUnavailability.objects.create(volunteer_shift=self.volunteer_shift,
                                                                               date='2016-12-26')
        self.volunteer_presence = VolunteerPresence.objects.create(volunteer_shift=self.volunteer_shift,
                                                                   date='2016-12-27', presence=True)

        self.factory = RequestFactory()

    def test_Volunteer(self):
        self.assertEqual(str(self.user.volunteer), self.user.get_username())

        self.user.first_name = 'ReFood'
        self.user.last_name = 'Cascais CPR'
        self.user.save()

        self.assertEqual(str(self.user.volunteer), self.user.get_full_name())

    def test_Task(self):
        self.assertEqual(str(self.task), 'Distribuição')

    def test_Shift(self):
        self.assertEqual(str(self.shift), 'Distribuição (Segunda-feira)')

    def test_Preference(self):
        self.assertEqual(str(self.preference), '[1] refood - Distribuição (Segunda-feira)')

    def test_VolunteerShift(self):
        self.assertEqual(str(self.volunteer_shift), 'refood - Distribuição (Segunda-feira)')

    def test_VolunteerUnavailability(self):
        self.assertEqual(str(self.volunteer_unavailability),
                         '2016-12-26 - refood - Distribuição (Segunda-feira)')

    def test_VolunteerPresence(self):
        self.assertEqual(str(self.volunteer_presence), '2016-12-27 - refood - Distribuição (Segunda-feira)')

    def test_view_index(self):
        request = self.factory.get('/volunteers/')
        request.user = self.user
        response = index(request)
        self.assertContains(response, 'Volunteers by state')
