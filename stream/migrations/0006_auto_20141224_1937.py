# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stream', '0005_auto_20141224_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stream',
            name='end',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stream',
            name='start',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
