# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import project.models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_profile_reservation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='expiration',
            field=models.DateTimeField(default=project.models.a_time_in_the_future),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
