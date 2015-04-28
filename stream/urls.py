from django.conf.urls import patterns, url

from stream import views

urlpatterns = patterns('',
  url(r'^$', views.index, name='index'),
  url(r'^old/', views.old, name='old'),
  url(r'^test/', views.test, name='test'),
)