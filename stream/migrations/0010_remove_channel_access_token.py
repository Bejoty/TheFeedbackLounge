# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stream', '0009_auto_20150419_1134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='channel',
            name='access_token',
        ),
    ]
