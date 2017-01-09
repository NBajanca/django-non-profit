from django.conf.urls import url

from volunteers import views

app_name = 'volunteers'
urlpatterns = [
    url(r'^$', views.index, name='index'),
]