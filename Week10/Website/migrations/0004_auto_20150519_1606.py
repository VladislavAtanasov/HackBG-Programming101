# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0003_auto_20150519_1416'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projection',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('type', models.CharField(max_length=5)),
                ('data', models.CharField(max_length=12)),
                ('time', models.CharField(max_length=12)),
            ],
        ),
        migrations.RemoveField(
            model_name='movies',
            name='data',
        ),
        migrations.RemoveField(
            model_name='movies',
            name='time',
        ),
        migrations.RemoveField(
            model_name='movies',
            name='type',
        ),
        migrations.AddField(
            model_name='projection',
            name='movie',
            field=models.ForeignKey(to='Website.Movies'),
        ),
    ]
