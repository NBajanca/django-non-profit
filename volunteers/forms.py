from django.forms import ModelForm
from volunteers.models import Volunteer


class VolunteerForm(ModelForm):
    class Meta:
        model = Volunteer
        fields = ['date_of_birth', 'mobile_phone', 'car_availability', 'address', 'academic_qualifications',
                  'profession', 'volunteer_experience', 'observations']