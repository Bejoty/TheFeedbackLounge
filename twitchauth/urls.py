from django.conf.urls import patterns, url

from twitchauth import views

urlpatterns = patterns('',
    url(r'^$', views.auth, name='auth'),
    url(r'^test/', views.test, name='test'),
    url(r'^connect/', views.connect, name='connect'),
)
