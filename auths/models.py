# python packages imports
from datetime import datetime 
# django core packeges imports
from django.db import models
from django.contrib.auth.models import User


class Information(models.Model):
	""" This is class which stores all information about particular user """

	user = models.OneToOneField(User, primary_key=True, verbose_name='ползователь')
	phone_number = models.IntegerField('номер телефона')
	photo = models.ImageField('фото', upload_to='media', null=True, blank=True)

	def __unicode__(self):
		return self.user.first_name + " " + self.user.last_name

	class Meta:
		verbose_name = "инфо пользователя"
		verbose_name_plural = "инфо пользователей"

class Verification(models.Model):
	""" Class to verify user's email """

	is_verified = models.BooleanField('подтвержден ?', default=False)
	user = models.OneToOneField(User, primary_key=True, verbose_name='ползователь')
	email = models.EmailField('Email', max_length=100)
	random_string = models.CharField('random_string', max_length=32)

	def __unicode__(self):
		return self.user.username

