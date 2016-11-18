from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from volunteers.views import ProfileView

app_name = 'volunteers'
urlpatterns = [
    url(r'^profile/(?P<pk>[0-9]+)/$', login_required(ProfileView.as_view()), name='profile'),
]