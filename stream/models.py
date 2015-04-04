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