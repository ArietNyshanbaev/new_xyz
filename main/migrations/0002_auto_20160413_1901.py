# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instance_buy',
            name='price',
            field=models.IntegerField(default=-1, null=True, verbose_name=b'\xd1\x86\xd0\xb5\xd0\xbd\xd0\xb0', blank=True),
        ),
    ]
