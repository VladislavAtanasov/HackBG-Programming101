# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0002_remove_movies_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='data',
            field=models.CharField(max_length=12, default=datetime.datetime(2015, 5, 19, 14, 15, 46, 188062, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movies',
            name='time',
            field=models.CharField(max_length=12, default='21:00'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movies',
            name='type',
            field=models.CharField(max_length=5, default='2D'),
            preserve_default=False,
        ),
    ]
