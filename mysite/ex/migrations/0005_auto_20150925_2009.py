# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ex', '0004_auto_20150924_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='titles',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='titles',
            name='ressource',
            field=models.ForeignKey(to='ex.Gallery'),
        ),
    ]
