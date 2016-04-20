# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fishkas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imei',
            name='imei',
            field=models.CharField(unique=True, max_length=50, verbose_name=b'imei'),
        ),
    ]
