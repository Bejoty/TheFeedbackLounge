from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User)
    display_name = models.CharField(max_length=25)
    logo_url = models.URLField()
    bio = models.CharField(max_length=300)
    access_token = models.CharField(max_length=50)

    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
      return self.display_name
