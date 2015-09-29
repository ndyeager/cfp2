# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fellow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('full_name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('current_position', models.CharField(max_length=100)),
                ('bio', models.TextField()),
                ('year', models.IntegerField(default=0)),
                ('image', models.ImageField(height_field=140, width_field=140, upload_to=b'img/profile')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('full_name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('bio', models.TextField()),
                ('image', models.ImageField(height_field=140, width_field=140, upload_to=b'img/profile')),
            ],
        ),
    ]
