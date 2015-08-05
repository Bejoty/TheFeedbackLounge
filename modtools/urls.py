from django.conf.urls import patterns, url

from modtools import views

urlpatterns = patterns('',
    url(r'^viewers/', views.viewers, name='viewers'),
)
