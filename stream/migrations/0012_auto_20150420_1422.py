# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stream', '0011_auto_20150420_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='state',
            field=models.CharField(default='offline', max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='channel',
            name='viewers',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
