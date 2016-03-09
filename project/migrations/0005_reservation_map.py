# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_auto_20160308_0246'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='map',
            field=models.CharField(default='city', max_length=100),
            preserve_default=False,
        ),
    ]
