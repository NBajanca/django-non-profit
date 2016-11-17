"""django_non_profit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from main import views
from main.forms import CaptchaPasswordResetForm

app_name = 'main'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'login/$', auth_views.login, {'template_name': 'main/login.html'}, name='login'),
    url(r'logout/$', auth_views.logout, {'template_name': 'main/logout.html'}, name='logout'),
    url(r'^locked/$', views.locked_out, name='locked_out'),
    url(r'password_reset/$', auth_views.password_reset,
        {'template_name': 'main/password_reset.html', 'email_template_name': 'main/email/password_reset_email.html',
         'subject_template_name': 'main/email/password_reset_subject.txt',
         'password_reset_form': CaptchaPasswordResetForm, 'post_reset_redirect': 'main:password_reset_done'},
        name='password_reset'),
    url(r'password_reset/done/$', auth_views.password_reset_done, {'template_name': 'main/password_reset_done.html'},
        name='password_reset_done'),
    url(r'password_reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, {'template_name': 'main/password_reset_confirm.html',
                                            'post_reset_redirect': 'main:password_reset_complete',},
        name='password_reset_confirm'),
    url(r'password_reset/complete/$', auth_views.password_reset_complete,
        {'template_name': 'main/password_reset_complete.html'}, name='password_reset_complete'),
]
