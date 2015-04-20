import datetime
import urllib
import json
from django.db import models
from django.utils import timezone


class Game(models.Model):
  title = models.CharField(max_length=50)
  code = models.CharField(max_length=5)

  def __str__(self):
    return self.title


class Stream(models.Model):
  featured_game = models.ForeignKey(Game, null=True, blank=True)

  date = models.DateField()
  start = models.TimeField(null=True, blank=True)
  end = models.TimeField(null=True, blank=True)

  description = models.TextField(default="", blank=True)


class Channel(models.Model):
  name = models.CharField(max_length=25)

  display_name = models.CharField(max_length=25)
  status = models.CharField(max_length=250)
  game = models.CharField(max_length=50)
  views = models.IntegerField(default=0)
  followers = models.IntegerField(default=0)

  state = models.CharField(max_length=25)
  viewers = models.IntegerField(default=0)

  url = models.URLField()
  logo_url = models.URLField()
  video_banner_url = models.URLField()
  profile_banner_url = models.URLField()

  last_updated = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.display_name

  def recently_updated(self):
    return self.last_updated >= timezone.now() - datetime.timedelta(minutes=1)

  def update(self):
    #TODO: Client ID header to avoid rate limiting

    req = urllib.request.Request('https://api.twitch.tv/kraken/channels/' + self.name)
    res = urllib.request.urlopen(req)
    channel_data = json.loads(res.read().decode('utf-8'))

    self.display_name = channel_data['display_name']
    self.status = channel_data['status']
    self.game = channel_data['game']
    self.views = channel_data['views']
    self.followers = channel_data['followers']

    self.url = channel_data['url']
    self.logo_url = channel_data['logo']
    self.video_banner_url = channel_data['video_banner']
    self.profile_banner_url = channel_data['profile_banner']

    req = urllib.request.Request('https://api.twitch.tv/kraken/streams/' + self.name)
    res = urllib.request.urlopen(req)
    stream_data = json.loads(res.read().decode('utf-8'))

    self.state = 'offline'

    if stream_data['stream']:
      self.state = 'live'
      stream = stream_data['stream']
      self.video_banner_url = stream['preview']['medium']
      self.viewers = stream['viewers']

    self.save()
