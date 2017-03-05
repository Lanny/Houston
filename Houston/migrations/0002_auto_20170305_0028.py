# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('Houston', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pageview',
            name='query',
            field=models.CharField(default=b'', max_length=1024),
        ),
        migrations.AlterField(
            model_name='pageview',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
