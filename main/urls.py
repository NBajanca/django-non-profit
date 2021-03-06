from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from main import views
from main.forms import CaptchaPasswordResetForm
from main.views import ProfileView

app_name = 'main'
urlpatterns = [
    url(r'^$', views.index, name='index'),

    # Profile
    url(r'^profile/(?P<pk>[0-9]+)/$', login_required(ProfileView.as_view()), name='profile'),
    url(r'^edit-profile/(?P<pk>[0-9]+)/$', views.edit_profile, name='edit_profile'),
    url(r'^edit-profile/user/(?P<pk>[0-9]+)/$', views.edit_profile_user, name='edit_profile_user'),
    url(r'^edit-profile/password/(?P<pk>[0-9]+)/$', views.edit_profile_password, name='edit_profile_password'),
    url(r'^edit-profile/email/(?P<pk>[0-9]+)/$', views.edit_profile_email, name='edit_profile_email'),
    url(r'^edit-profile/extended/(?P<pk>[0-9]+)/$', views.edit_profile_extended, name='edit_profile_extended'),


    # Auth
    url(r'login/$', auth_views.login, {'template_name': 'auth/login.html'}, name='login'),
    url(r'logout/$', auth_views.logout, {'template_name': 'auth/logout.html'}, name='logout'),
    url(r'^locked/$', views.locked_out, name='locked_out'),
    url(r'password_reset/$', auth_views.password_reset,
        {'template_name': 'auth/password_reset.html', 'email_template_name': 'main/email/password_reset_email.html',
         'subject_template_name': 'main/email/password_reset_subject.txt',
         'password_reset_form': CaptchaPasswordResetForm, 'post_reset_redirect': 'main:password_reset_done'},
        name='password_reset'),
    url(r'password_reset/done/$', auth_views.password_reset_done, {'template_name': 'auth/password_reset_done.html'},
        name='password_reset_done'),
    url(r'password_reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, {'template_name': 'auth/password_reset_confirm.html',
                                            'post_reset_redirect': 'main:password_reset_complete'},
        name='password_reset_confirm'),
    url(r'password_reset/complete/$', auth_views.password_reset_complete,
        {'template_name': 'auth/password_reset_complete.html'}, name='password_reset_complete'),
]
