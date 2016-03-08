# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import project.models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20160308_0131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='password',
            field=models.CharField(default=project.models.random_password, max_length=100),
        ),
    ]
