# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stream', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stream',
            name='day_off',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='stream',
            name='description',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stream',
            name='end',
            field=models.TimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='stream',
            name='featured_game',
            field=models.ForeignKey(to='stream.Game', blank=True),
        ),
        migrations.AlterField(
            model_name='stream',
            name='start',
            field=models.TimeField(blank=True),
        ),
    ]
