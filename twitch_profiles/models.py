from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User)
    display_name = models.CharField(max_length=25)
    logo = models.ImageField(upload_to='profile')
    bio = models.CharField(max_length=300)
    access_token = models.CharField(max_length=50)

    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)