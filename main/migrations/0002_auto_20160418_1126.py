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
            name='max_price',
            field=models.IntegerField(default=-1, null=True, verbose_name=b'\xd0\xbc\xd0\xb0\xd0\xba\xd1\x81\xd0\xb8\xd0\xbc\xd0\xb0\xd0\xbb\xd1\x8c\xd0\xbd\xd0\xb0\xd1\x8f \xd1\x86\xd0\xb5\xd0\xbda', blank=True),
        ),
        migrations.AlterField(
            model_name='instance_buy',
            name='min_price',
            field=models.IntegerField(default=-1, null=True, verbose_name=b'\xd0\xbc\xd0\xb8\xd0\xbd\xd0\xb8\xd0\xbc\xd0\xb0\xd0\xbb\xd1\x8c\xd0\xbd\xd0\xb0\xd1\x8f \xd1\x86\xd0\xb5\xd0\xbda', blank=True),
        ),
    ]
