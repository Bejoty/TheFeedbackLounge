from django.conf.urls import patterns, url

from base import views

urlpatterns = patterns('',
    url(r'^$', views.base, name='base'),
    url(r'^test/', views.test, name='test'),
)