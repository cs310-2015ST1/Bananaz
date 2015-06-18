# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('garden', '0006_auto_20150617_1829'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Account',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(null=True, to='garden.User'),
        ),
    ]
