# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stream', '0008_channel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='channel',
            old_name='profile_baner_url',
            new_name='profile_banner_url',
        ),
    ]
