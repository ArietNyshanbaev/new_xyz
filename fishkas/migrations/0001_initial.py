# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Best_deal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=100, verbose_name=b'\xd0\xba\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb3\xd0\xbe\xd1\x80\xd0\xb8\xd0\xb8')),
                ('added_date', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'\xd0\xb4\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xb4\xd0\xbe\xd0\xb1\xd0\xb0\xd0\xb2\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f')),
                ('instance', models.ForeignKey(verbose_name=b'instance', blank=True, to='main.Instance', null=True)),
            ],
            options={
                'verbose_name': '\u043b\u0443\u0447\u0448\u0435\u0435 \u043f\u0440\u0435\u0434\u043b\u043e\u0436\u0435\u043d\u0438\u0435',
                'verbose_name_plural': '\u043b\u0443\u0447\u0448\u0438\u0435 \u043f\u0440\u0435\u0434\u043b\u043e\u0436\u0435\u043d\u0438\u044f ',
            },
        ),
        migrations.CreateModel(
            name='Image_of_Instance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'media', verbose_name=b'image')),
                ('instance', models.ForeignKey(to='main.Instance')),
            ],
        ),
        migrations.CreateModel(
            name='Imei',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imei', models.IntegerField(unique=True, verbose_name=b'imei')),
                ('contact_telephone', models.CharField(max_length=50, verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xbd\xd1\x82\xd0\xb0\xd0\xba\xd1\x82\xd0\xbd\xd1\x8b\xd0\xb5 \xd0\xb4\xd0\xb0\xd0\xbd\xd0\xbd\xd1\x8b\xd0\xb5')),
                ('owner', models.CharField(max_length=70, verbose_name=b'\xd0\x92\xd0\xbb\xd0\xb0\xd0\xb4\xd0\xb5\xd0\xbb\xd0\xb5\xd1\x86')),
                ('instance', models.ForeignKey(to='main.Instance')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.CharField(max_length=1000, null=True, verbose_name=b'\xd1\x81\xd0\xbe\xd0\xbe\xd0\xb1\xd1\x89\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5', blank=True)),
                ('username', models.CharField(max_length=100, null=True, verbose_name=b'\xd0\xbf\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c', blank=True)),
                ('sent_date', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'\xd0\xbf\xd0\xbe\xd0\xbb\xd1\x83\xd1\x87\xd0\xb5\xd0\xbd\xd0\xbe')),
            ],
            options={
                'verbose_name': '\u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435',
                'verbose_name_plural': '\u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f',
            },
        ),
        migrations.CreateModel(
            name='Notifier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('min_price', models.IntegerField(default=0, verbose_name=b'\xd0\xbc\xd0\xb8\xd0\xbd\xd0\xb8\xd0\xbc\xd0\xb0\xd0\xbb\xd1\x8c\xd0\xbd\xd0\xb0\xd1\x8f \xd1\x81\xd1\x83\xd0\xbc\xd0\xbc\xd0\xb0')),
                ('max_price', models.IntegerField(default=0, verbose_name=b'\xd0\xbc\xd0\xb0\xd0\xba\xd1\x81\xd0\xb8\xd0\xbc\xd0\xb0\xd0\xbb\xd1\x8c\xd0\xbd\xd0\xb0\xd1\x8f \xd1\x81\xd1\x83\xd0\xbc\xd0\xbc\xd0\xb0')),
                ('categories', models.CharField(max_length=1000, verbose_name=b'id \xd0\xba\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb3\xd0\xbe\xd1\x80\xd0\xb8\xd0\xb9')),
                ('user', models.ForeignKey(default=0, verbose_name=b'\xd0\xbf\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Slogan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=100, verbose_name=b'\xd1\x81\xd0\xbb\xd0\xbe\xd0\xb3\xd0\xb0\xd0\xbd')),
            ],
            options={
                'verbose_name': '\u0441\u043b\u043e\u0433\u0430\u043d',
                'verbose_name_plural': '\u0441\u043b\u043e\u0433\u0430\u043d\u044b',
            },
        ),
        migrations.CreateModel(
            name='Wish',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('for_buy', models.BooleanField(default=False)),
                ('instance', models.ForeignKey(verbose_name=b'instance', blank=True, to='main.Instance', null=True)),
                ('instance_buy', models.ForeignKey(verbose_name=b'instance buy', blank=True, to='main.Instance_buy', null=True)),
                ('user', models.ForeignKey(verbose_name=b'\xd0\xbf\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u0436\u0435\u043b\u0430\u0435\u043c\u044b\u0439',
                'verbose_name_plural': '\u0436\u0435\u043b\u0430\u0435\u043c\u044b\u0435',
            },
        ),
    ]
