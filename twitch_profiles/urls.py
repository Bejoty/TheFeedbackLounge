from django.conf.urls import url

from twitch_profiles import views

urlpatterns = [
    url(r'^(?P<username>\w+)/$', views.view, name='view'),
]
