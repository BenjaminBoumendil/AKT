# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('ex', '0009_auto_20150927_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='titles',
            name='id',
            field=models.UUIDField(primary_key=True, default=uuid.uuid4, serialize=False, editable=False, verbose_name='id'),
        ),
    ]
