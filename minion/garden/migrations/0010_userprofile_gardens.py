# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('garden', '0009_auto_20150708_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='gardens',
            field=models.ManyToManyField(to='garden.Garden'),
        ),
    ]
