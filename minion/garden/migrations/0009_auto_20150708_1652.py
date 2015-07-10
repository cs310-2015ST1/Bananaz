# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('garden', '0008_auto_20150617_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='oauth_token',
            field=models.TextField(default='sbbbdkbf'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='oauth_token_secret',
            field=models.TextField(default='vaastavsucks'),
            preserve_default=False,
        ),
    ]
