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
    req = urllib.request.Request('https://api.twitch.tv/kraken/channels/' + self.name)
    res = urllib.request.urlopen(req)
    data = json.loads(res.read().decode('utf-8'))

    self.display_name = data['display_name']
    self.status = data['status']
    self.game = data['game']
    self.views = data['views']
    self.followers = data['followers']

    self.url = data['url']
    self.logo_url = data['logo']
    self.video_banner_url = data['video_banner']
    self.profile_banner_url = data['profile_banner']

    self.save()
