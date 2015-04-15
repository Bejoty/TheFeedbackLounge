from django.db import models


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
  access_token = models.CharField(max_length=50)

  status = models.CharField(max_length=50)
  game = models.CharField(max_length=50)
  views = models.IntegerField()
  followers = models.IntegerField()

  url = models.URLField()
  logo_url = models.URLField()
  video_banner_url = models.URLField()
  profile_baner_url = models.URLField()

  last_updated = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.display_name
