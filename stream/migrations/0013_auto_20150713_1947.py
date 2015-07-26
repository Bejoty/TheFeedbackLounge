# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stream', '0012_auto_20150420_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='game',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
