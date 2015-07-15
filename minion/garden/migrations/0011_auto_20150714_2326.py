# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('garden', '0010_userprofile_gardens'),
    ]

    operations = [
        migrations.CreateModel(
            name='GardenUserRelationship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_saved', models.DateTimeField(auto_now_add=True)),
                ('garden', models.ForeignKey(to='garden.Garden')),
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='gardens',
        ),
        migrations.AddField(
            model_name='gardenuserrelationship',
            name='userprofile',
            field=models.ForeignKey(to='garden.UserProfile'),
        ),
    ]
