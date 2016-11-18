from django.contrib.auth.models import User
from django.forms import model_to_dict
from django.views.generic import DetailView


class ProfileView(DetailView):
    model = User
    template_name = 'volunteers/profile.html'


