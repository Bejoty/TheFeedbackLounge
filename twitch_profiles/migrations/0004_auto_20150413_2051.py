# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitch_profiles', '0003_auto_20150328_2049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='logo',
        ),
        migrations.AddField(
            model_name='profile',
            name='logo_url',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]
