# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stream', '0007_remove_stream_day_off'),
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('display_name', models.CharField(max_length=25)),
                ('access_token', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('game', models.CharField(max_length=50)),
                ('views', models.IntegerField()),
                ('followers', models.IntegerField()),
                ('url', models.URLField()),
                ('logo_url', models.URLField()),
                ('video_banner_url', models.URLField()),
                ('profile_baner_url', models.URLField()),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
