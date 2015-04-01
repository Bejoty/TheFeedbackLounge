# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stream', '0006_auto_20141224_1937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stream',
            name='day_off',
        ),
    ]
