# python packages import
from datetime import datetime
# django core packages imports
from django.db import models
from django.contrib.auth.models import User
# project models imprt
from main.models import Instance

class Wish(models.Model):
	""" Wish class for wish list """

	user = models.ForeignKey(User, verbose_name='пользователь')
	instance = models.ForeignKey(Instance, verbose_name='instance', null=True, blank=True)

	def __unicode__(self):
		return self.user.username + " " + str(self.instance_id)

	class Meta:
		verbose_name = "желаемый"
		verbose_name_plural = "желаемые"

class Message(models.Model):
	""" Message class for us kind a feedback """

	message = models.CharField('сообщение', max_length=1000, null=True, blank=True)

	def __unicode__(self):
		return self.message[:20]

	class Meta:
		verbose_name = "сообщение"
		verbose_name_plural = "сообщения"

class Best_deal(models.Model):
	""" Best_deal class for Luchwee predlojenie dnay """

	instance = models.ForeignKey(Instance, verbose_name='instance', null=True, blank=True)
	category = models.CharField('категории', max_length=100)
	added_date = models.DateTimeField('дата добавления', default=datetime.now)

	def __unicode__(self):
		return self.category

	class Meta:
		verbose_name = "лучшее предложение"
		verbose_name_plural = "лучшие предложения "

class Slogan(models.Model):
	""" Slogan class for the slogn on topbar """
	text = models.CharField('слоган', max_length=100)

	def __unicode__(self):
		return self.text[:20]

	class Meta:
		verbose_name = "слоган"
		verbose_name_plural = "слоганы"

class Notifier(models.Model):
	""" class for Notify me function """

	min_price = models.IntegerField('минимальная сумма', default=0)
	max_price = models.IntegerField('максимальная сумма', default=0)
	user = models.ForeignKey(User, verbose_name='пользователь', default=0)
	categories = models.CharField('id категорий', max_length=1000)

	def __unicode__(self):
		return self.user.username + " from " + str(self.min_price) + " to " + str(self.max_price)
		