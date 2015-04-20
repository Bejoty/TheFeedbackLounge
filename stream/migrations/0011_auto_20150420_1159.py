# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stream', '0010_remove_channel_access_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='followers',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='channel',
            name='status',
            field=models.CharField(max_length=250),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='channel',
            name='views',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
