# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('garden', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='garden',
            name='latitude',
            field=models.DecimalField(max_digits=30, decimal_places=20),
        ),
        migrations.AlterField(
            model_name='garden',
            name='longitude',
            field=models.DecimalField(max_digits=30, decimal_places=20),
        ),
    ]
