from django.conf.urls import include, url
from django.contrib import admin

from zach import views
import twitch_profiles
import twitchauth

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^stream/', include('stream.urls', namespace='stream')),
    url(r'^twitchauth/', include('twitchauth.urls', namespace='twitchauth')),
    url(r'^connect/', twitchauth.views.connect, name='connect'),
    url(r'^logout/', twitchauth.views.logout_user, name='logout'),
    url(r'^auth/', twitchauth.views.auth, name='authenticate'),
    # url(r'^news/', include('zinnia.urls', namespace='zinnia')),
    # url(r'^comments/', include('django_comments.urls')),
    url(r'^u/', include('twitch_profiles.urls', namespace='profiles')),
    url(r'^sessiontest/', twitch_profiles.views.session_test, name='test'),
    url(r'^modtools/', include('modtools.urls', namespace='modtools')),
    url(r'^(?P<username>\w+)/$', twitch_profiles.views.view, name='view'),
]
