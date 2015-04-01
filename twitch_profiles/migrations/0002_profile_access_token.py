# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitch_profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='access_token',
            field=models.CharField(default='invalidtoken', max_length=20),
            preserve_default=False,
        ),
    ]
