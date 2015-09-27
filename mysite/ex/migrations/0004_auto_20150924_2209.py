# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ex', '0003_gallery_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Titles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('vote', models.IntegerField(default=0, verbose_name='vote')),
            ],
        ),
        migrations.AlterField(
            model_name='gallery',
            name='name',
            field=models.CharField(max_length=255, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='titles',
            name='ressource',
            field=models.OneToOneField(to='ex.Gallery'),
        ),
    ]
