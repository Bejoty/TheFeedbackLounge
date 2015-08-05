from django.conf.urls import patterns, url

from twitch_profiles import views

urlpatterns = patterns('',
    url(r'^(?P<username>\w+)/$', views.view, name='view'),
)
