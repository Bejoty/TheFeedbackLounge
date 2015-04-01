from django.conf.urls import patterns, include, url
from django.contrib import admin

from zach import views
import twitch_profiles

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'zach.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^base/', include('base.urls', namespace='base')),
    url(r'^stream/', include('stream.urls', namespace='stream')),
    url(r'^twitchauth/', include('twitchauth.urls', namespace='twitchauth')),
    url(r'^u/', include('twitch_profiles.urls', namespace='profiles')),
    url(r'^sessiontest/', twitch_profiles.views.session_test, name='test'),
    url(r'^(?P<username>\w+)/$', twitch_profiles.views.view, name='view'),
)
