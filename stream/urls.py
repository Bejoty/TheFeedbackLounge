from django.conf.urls import url

from stream import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^old/', views.old, name='old'),
    url(r'^test/', views.test, name='test'),
]
