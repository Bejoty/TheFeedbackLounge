from django.conf.urls import url

from modtools import views

urlpatterns = [
    url(r'^viewers/', views.viewers, name='viewers'),
]
