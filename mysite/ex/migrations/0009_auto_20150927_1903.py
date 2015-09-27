# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ex', '0008_auto_20150926_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='titles',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Title', blank=True),
        ),
    ]
