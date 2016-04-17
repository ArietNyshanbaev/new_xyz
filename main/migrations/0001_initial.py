# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name=b'\xd0\xb1\xd1\x80\xd0\xb5\xd0\xbd\xd0\xb4')),
                ('image', models.ImageField(upload_to=b'media', null=True, verbose_name=b'\xd1\x84\xd0\xbe\xd1\x82\xd0\xbe1', blank=True)),
            ],
            options={
                'verbose_name': '\u0431\u0440\u0435\u043d\u0434',
                'verbose_name_plural': '\u0431\u0440\u0435\u043d\u0434\u044b',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name=b'\xd0\xba\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb3\xd0\xbe\xd1\x80\xd0\xb8\xd1\x8f')),
                ('icon', models.CharField(max_length=100, null=True, verbose_name=b'\xd0\xb8\xd0\xba\xd0\xbe\xd0\xbd\xd0\xba\xd0\xb0', blank=True)),
                ('tree_level', models.IntegerField(null=True, verbose_name=b'\xd0\xb3\xd0\xbb\xd1\x83\xd0\xb1\xd0\xb8\xd0\xbd\xd0\xb0 \xd0\xba\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb3\xd0\xbe\xd1\x80\xd0\xb8\xd0\xb8', blank=True)),
            ],
            options={
                'verbose_name': '\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f',
                'verbose_name_plural': '\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xb3\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb4\xd0\xb0')),
            ],
            options={
                'verbose_name': '\u0433\u043e\u0440\u043e\u0434',
                'verbose_name_plural': '\u0433\u043e\u0440\u043e\u0434\u0430',
            },
        ),
        migrations.CreateModel(
            name='Instance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('color', models.CharField(max_length=100, verbose_name=b'\xd1\x86\xd0\xb2\xd0\xb5\xd1\x82')),
                ('added_date', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'\xd0\xb4\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xb4\xd0\xbe\xd0\xb1\xd0\xb0\xd0\xb2\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f')),
                ('updated_date', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'\xd0\xb4\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbe\xd0\xb1\xd0\xbd\xd0\xbe\xd0\xb2\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f (up!)')),
                ('telephones', models.CharField(max_length=100, null=True, verbose_name=b'\xd1\x82\xd0\xb5\xd0\xbb\xd0\xb5\xd1\x84\xd0\xbe\xd0\xbd', blank=True)),
                ('note', models.TextField(null=True, verbose_name=b'\xd0\xbe\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5', blank=True)),
                ('price', models.IntegerField(null=True, verbose_name=b'\xd1\x86\xd0\xb5\xd0\xbd\xd0\xb0', blank=True)),
                ('photo1', models.ImageField(upload_to=b'media', null=True, verbose_name=b'\xd1\x84\xd0\xbe\xd1\x82\xd0\xbe1', blank=True)),
                ('photo2', models.ImageField(upload_to=b'media', null=True, verbose_name=b'\xd1\x84\xd0\xbe\xd1\x82\xd0\xbe2', blank=True)),
                ('photo3', models.ImageField(upload_to=b'media', null=True, verbose_name=b'\xd1\x84\xd0\xbe\xd1\x82\xd0\xbe3', blank=True)),
                ('exchange', models.BooleanField(default=False, verbose_name=b'\xd0\xbe\xd0\xb1\xd0\xbc\xd0\xb5\xd0\xbd')),
                ('bargain', models.BooleanField(default=False, verbose_name=b'\xd1\x82\xd0\xbe\xd1\x80\xd0\xb3')),
                ('guarantee', models.CharField(max_length=100, null=True, verbose_name=b'\xd0\xb3\xd0\xb0\xd1\x80\xd0\xb0\xd0\xbd\xd1\x82\xd0\xb8\xd1\x8f', blank=True)),
                ('smartphone', models.BooleanField(default=False, verbose_name=b'\xd1\x81\xd0\xbc\xd0\xb0\xd1\x80\xd1\x82\xd1\x84\xd0\xbe\xd0\xbd')),
                ('notebook', models.BooleanField(default=False, verbose_name=b'\xd0\xbd\xd0\xbe\xd1\x83\xd1\x82\xd0\xb1\xd1\x83\xd0\xba')),
                ('tablet', models.BooleanField(default=False, verbose_name=b'\xd0\xbf\xd0\xbb\xd0\xb0\xd0\xbd\xd1\x88\xd0\xb5\xd1\x82')),
                ('other', models.BooleanField(default=False, verbose_name=b'\xd0\xb0\xd0\xba\xd1\x81\xd0\xb5\xd1\x81\xd1\x81\xd1\x83\xd0\xb0\xd1\x80\xd1\x8b')),
                ('modell', models.CharField(max_length=b'100', null=True, verbose_name=b'\xd0\xbc\xd0\xbe\xd0\xb4\xd0\xb5\xd0\xbb\xd1\x8c', blank=True)),
                ('condition', models.CharField(max_length=b'100', null=True, verbose_name=b'\xd1\x81\xd0\xbe\xd1\x81\xd1\x82\xd0\xbe\xd1\x8f\xd0\xbd\xd0\xb8\xd0\xb5', blank=True)),
                ('documents', models.BooleanField(default=False, verbose_name=b'\xd0\xb4\xd0\xbe\xd0\xba\xd1\x83\xd0\xbc\xd0\xb5\xd0\xbd\xd1\x82\xd1\x8b')),
                ('box', models.BooleanField(default=False, verbose_name=b'\xd0\xba\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb1\xd0\xba\xd0\xb0')),
                ('earpods', models.BooleanField(default=False, verbose_name=b'\xd0\xbd\xd0\xb0\xd1\x83\xd1\x88\xd0\xbd\xd0\xb8\xd0\xba\xd0\xb8')),
                ('memory', models.IntegerField(null=True, verbose_name=b'\xd0\xbf\xd0\xb0\xd0\xbc\xd1\x8f\xd1\x82\xd1\x8c', blank=True)),
                ('title', models.CharField(max_length=100, null=True, verbose_name=b'\xd0\xbe\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd1\x82\xd0\xb5\xd0\xbc\xd1\x8b', blank=True)),
                ('linker', models.CharField(default=b'', max_length=1000, null=True, verbose_name=b'\xd1\x81\xd1\x81\xd1\x8b\xd0\xbb\xd0\xba\xd0\xb0', blank=True)),
                ('city', models.ForeignKey(default=1, verbose_name=b'\xd0\xb3\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb4', to='main.City')),
            ],
            options={
                'verbose_name': '\u043e\u0431\u044a\u044f\u0432\u043b\u0435\u043d\u0438\u0435',
                'verbose_name_plural': '\u043e\u0431\u044a\u044f\u0432\u043b\u0435\u043d\u0438\u044f',
            },
        ),
        migrations.CreateModel(
            name='Instance_buy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('added_date', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'\xd0\xb4\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xb4\xd0\xbe\xd0\xb1\xd0\xb0\xd0\xb2\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f')),
                ('updated_date', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'\xd0\xb4\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbe\xd0\xb1\xd0\xbd\xd0\xbe\xd0\xb2\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f (up!)')),
                ('telephones', models.CharField(max_length=100, null=True, verbose_name=b'\xd1\x82\xd0\xb5\xd0\xbb\xd0\xb5\xd1\x84\xd0\xbe\xd0\xbd', blank=True)),
                ('price', models.IntegerField(default=-1, null=True, verbose_name=b'\xd1\x86\xd0\xb5\xd0\xbd\xd0\xb0', blank=True)),
                ('smartphone', models.BooleanField(default=False, verbose_name=b'\xd1\x81\xd0\xbc\xd0\xb0\xd1\x80\xd1\x82\xd1\x84\xd0\xbe\xd0\xbd')),
                ('notebook', models.BooleanField(default=False, verbose_name=b'\xd0\xbd\xd0\xbe\xd1\x83\xd1\x82\xd0\xb1\xd1\x83\xd0\xba')),
                ('tablet', models.BooleanField(default=False, verbose_name=b'\xd0\xbf\xd0\xbb\xd0\xb0\xd0\xbd\xd1\x88\xd0\xb5\xd1\x82')),
                ('other', models.BooleanField(default=False, verbose_name=b'\xd0\xb0\xd0\xba\xd1\x81\xd0\xb5\xd1\x81\xd1\x81\xd1\x83\xd0\xb0\xd1\x80\xd1\x8b')),
                ('title', models.CharField(max_length=100, null=True, verbose_name=b'\xd0\xbe\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd1\x82\xd0\xb5\xd0\xbc\xd1\x8b', blank=True)),
                ('note', models.TextField(null=True, verbose_name=b'\xd0\xbe\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5', blank=True)),
                ('city', models.ForeignKey(default=1, verbose_name=b'\xd0\xb3\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb4', to='main.City')),
            ],
            options={
                'verbose_name': '\u043e\u0431\u044a\u044f\u0432\u043b\u0435\u043d\u0438\u0435 \u043a\u0443\u043f\u043b\u044e',
                'verbose_name_plural': '\u043e\u0431\u044a\u044f\u0432\u043b\u0435\u043d\u0438\u044f \u043a\u0443\u043f\u043b\u044e',
            },
        ),
        migrations.CreateModel(
            name='Modell',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name=b'\xd0\xbc\xd0\xbe\xd0\xb4\xd0\xb5\xd0\xbb\xd1\x8c')),
                ('is_not_unique', models.BooleanField(default=False)),
                ('year', models.IntegerField(null=True, verbose_name=b'\xd0\xb3\xd0\xbe\xd0\xb4 \xd0\xb2\xd1\x8b\xd0\xbf\xd1\x83\xd1\x81\xd0\xba\xd0\xb0', blank=True)),
                ('display', models.CharField(max_length=100, null=True, verbose_name=b'\xd0\xb4\xd1\x8e\xd0\xb9\xd0\xbc', blank=True)),
                ('os', models.CharField(max_length=100, null=True, verbose_name=b'\xd0\xbe\xd0\xbf\xd0\xb5\xd1\x80\xd0\xb0\xd1\x86\xd0\xb8\xd0\xbe\xd0\xbd\xd0\xbd\xd0\xb0\xd1\x8f \xd1\x81\xd0\xb8\xd1\x81\xd1\x82\xd0\xb5\xd0\xbc\xd0\xb0', blank=True)),
                ('cpu', models.CharField(max_length=100, null=True, verbose_name=b'cpu', blank=True)),
                ('camera', models.IntegerField(null=True, verbose_name=b'\xd0\xbe\xd1\x81\xd0\xbd\xd0\xbe\xd0\xb2\xd0\xbd\xd0\xb0\xd1\x8f \xd0\xba\xd0\xb0\xd0\xbc\xd0\xb5\xd1\x80\xd0\xb0', blank=True)),
                ('wifi', models.BooleanField(default=False, verbose_name=b'wifi')),
                ('bluetooth', models.BooleanField(default=False, verbose_name=b'bluetooth')),
                ('lte', models.BooleanField(default=False, verbose_name=b'4G')),
                ('memory', models.IntegerField(null=True, verbose_name=b'\xd0\xbe\xd0\xbf\xd0\xb5\xd1\x80\xd0\xb0\xd1\x82\xd0\xb8\xd0\xb2\xd0\xba\xd0\xb0', blank=True)),
                ('photo1', models.ImageField(upload_to=b'media', null=True, verbose_name=b'\xd1\x84\xd0\xbe\xd1\x82\xd0\xbe1', blank=True)),
                ('photo2', models.ImageField(upload_to=b'media', null=True, verbose_name=b'\xd1\x84\xd0\xbe\xd1\x82\xd0\xbe2', blank=True)),
                ('photo3', models.ImageField(upload_to=b'media', null=True, verbose_name=b'\xd1\x84\xd0\xbe\xd1\x82\xd0\xbe3', blank=True)),
                ('brand', models.ForeignKey(verbose_name=b'\xd0\xb1\xd1\x80\xd0\xb5\xd0\xbd\xd0\xb4', to='main.Brand')),
            ],
            options={
                'verbose_name': '\u043c\u043e\u0434\u0435\u043b\u044c',
                'verbose_name_plural': '\u043c\u043e\u0434\u0435\u043b\u0438',
            },
        ),
        migrations.CreateModel(
            name='Sold',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'\xd0\xb4\xd0\xb0\xd1\x82\xd0\xb0 \xd1\x83\xd0\xb4\xd0\xb0\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f')),
                ('date_added', models.DateTimeField(verbose_name=b'\xd0\xb4\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xb4\xd0\xbe\xd0\xb1\xd0\xb0\xd0\xb2\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f')),
                ('price', models.IntegerField(default=-1, verbose_name=b'\xd1\x86\xd0\xb5\xd0\xbd\xd0\xb0')),
                ('sold_at_ibox', models.BooleanField(default=False)),
                ('model', models.ForeignKey(verbose_name=b'\xd0\xbc\xd0\xbe\xd0\xb4\xd0\xb5\xd0\xbb\xd1\x8c', to='main.Modell')),
                ('seller', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': '\u043f\u0440\u043e\u0434\u0430\u043d\u043d\u044b\u0439',
                'verbose_name_plural': '\u043f\u0440\u043e\u0434\u0430\u043d\u043d\u044b\u0435',
            },
        ),
        migrations.AddField(
            model_name='instance_buy',
            name='model',
            field=models.ForeignKey(verbose_name=b'\xd0\xbc\xd0\xbe\xd0\xb4\xd0\xb5\xd0\xbb\xd1\x8c', to='main.Modell'),
        ),
        migrations.AddField(
            model_name='instance_buy',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='instance',
            name='model',
            field=models.ForeignKey(verbose_name=b'\xd0\xbc\xd0\xbe\xd0\xb4\xd0\xb5\xd0\xbb\xd1\x8c', to='main.Modell'),
        ),
        migrations.AddField(
            model_name='instance',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='brand',
            name='category',
            field=models.ForeignKey(verbose_name=b'\xd0\xba\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb3\xd0\xbe\xd1\x80\xd0\xb8\xd1\x8f', to='main.Category'),
        ),
    ]
