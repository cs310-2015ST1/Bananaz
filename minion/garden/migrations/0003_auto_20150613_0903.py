# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('garden', '0002_auto_20150606_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='garden',
            name='latitude',
            field=models.DecimalField(max_digits=10, decimal_places=7),
        ),
        migrations.AlterField(
            model_name='garden',
            name='longitude',
            field=models.DecimalField(max_digits=10, decimal_places=7),
        ),
    ]
