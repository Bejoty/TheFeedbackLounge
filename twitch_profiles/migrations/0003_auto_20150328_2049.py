# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitch_profiles', '0002_profile_access_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='access_token',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
    ]
