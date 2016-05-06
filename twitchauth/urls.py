from django.conf.urls import url

from twitchauth import views

urlpatterns = [
    url(r'^$', views.auth, name='auth'),
    url(r'^test/', views.test, name='test'),
    url(r'^connect/', views.connect, name='connect'),
]
