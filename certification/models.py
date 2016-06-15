from django.db import models
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db.models.signals import pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.utils.timezone import utc
# third party packages imports
from PIL import Image, ImageOps
# python packages imports
import StringIO
from datetime import datetime

class Category(models.Model):
    """ Category class which owns skill """

    title = models.CharField('категория', max_length=100)
    icon = models.CharField('иконка', max_length=100, null=True, blank=True)
    tree_level = models.IntegerField('глубина категории', null=True, blank=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"


class Brand(models.Model):
    """ Brand class which owned by Category """

    category = models.ForeignKey(Category, verbose_name='категория')
    title = models.CharField('бренд', max_length=100)
    image = models.ImageField('фото1', upload_to='media', null=True, blank=True)

    def __unicode__(self):
        return self.category.title + " " + self.title

    class Meta:
        verbose_name = "бренд"
        verbose_name_plural = "бренды"


class Modell(models.Model):
    """ Model class which owned by Brand """

    brand = models.ForeignKey(Brand, verbose_name='бренд')
    title = models.CharField('модель', max_length=100)
    is_not_unique = models.BooleanField(default=False)
    year = models.IntegerField('год выпуска', null=True, blank=True)
    display = models.CharField('дюйм', max_length=100, null=True, blank=True)
    os = models.CharField('операционная система', max_length=100, null=True, blank=True)
    cpu = models.CharField('cpu', max_length=100, null=True, blank=True)
    camera = models.IntegerField('основная камера', null=True, blank=True)
    wifi = models.BooleanField('wifi', default=False)
    bluetooth = models.BooleanField('bluetooth', default=False)
    lte = models.BooleanField('4G', default=False)
    memory = models.IntegerField('оперативка', null=True, blank=True)
    photo1 = models.ImageField('фото1', upload_to='media', null=True, blank=True)
    photo2 = models.ImageField('фото2', upload_to='media', null=True, blank=True)
    photo3 = models.ImageField('фото3', upload_to='media', null=True, blank=True)

    def __unicode__(self):
        return self.brand.category.title + " " + self.brand.title + " " + self.title

    class Meta:
        verbose_name = "модель"
        verbose_name_plural = "модели"

class CertifiedDevice(models.Model):
	""" Device class which are certified by iBox """

	color = models.CharField('цвет', max_length=100)
	created_date = models.DateTimeField('дата добавления', default=datetime.now)
	updated_date = models.DateTimeField('дата обновления (up!)', default=datetime.now)
	contacts = models.CharField('телефон', max_length=100, null=True, blank=True)
	description = models.TextField('описание', null=True, blank=True)
	price = models.IntegerField('цена', null=True, blank=True)
	user = models.ForeignKey(User, null=True, blank=True)
	model = models.ForeignKey(Modell, verbose_name='модель')
	guarantee = models.CharField('гарантия', max_length=100, null=True, blank=True)
	modell = models.CharField('модель', max_length='100', null=True, blank=True)
	condition = models.CharField('состояние', max_length='100', null=True, blank=True)
	memory = models.IntegerField('память', null=True, blank=True)
	title = models.CharField('описание темы', max_length=100, null=True, blank=True)
	imei = models.CharField('imei', max_length=16, default='0')

	def __unicode__(self):
		return unicode(self.model.title) + ' - '+ str(self.id)

	class Meta:
		verbose_name = "Certified объявление"
		verbose_name_plural = "Certified объявления"

class Photo(models.Model):
	device = models.ForeignKey(CertifiedDevice)
	photo = models.ImageField('фото', upload_to='media', null=True, blank=True)

	def save(self, *args, **kwargs):
		if self.photo:
			try:
				img = Image.open(StringIO.StringIO(self.photo.read()))

				if img.mode != 'RGB':
					img = img.convert('RGB')
				img_width = self.photo.width
				img_height = self.photo.height
				while img_width > 2200 or img_height > 2200:
					img_width /= 1.5
					img_height /= 1.5


				img.thumbnail((img_width, img_height), Image.ANTIALIAS)
				if img_width>img_height:
					size = (int(img_width),int(img_width*0.75))
				else:
					size = (int(img_height*1.34),int(img_height))

				image = img
				background = Image.new('RGBA', size, (255, 255, 255, 0))
				background.paste(image,((size[0] - image.size[0]) / 2, (size[1] - image.size[1]) / 2))

				output = StringIO.StringIO()
				background.save(output, format='JPEG', quality=90)
				output.seek(0)
				self.photo.delete(False)
				self.photo = InMemoryUploadedFile(output, 'ImageField', "file.jpg", 'image/jpeg', output.len, None)
			except IOError:
				pass
		super(Photo, self).save(*args, **kwargs)

	def __unicode__(self):
		return unicode(self.device.pk)

	class Meta:
		verbose_name = "Фото"
		verbose_name_plural = "Фотки"

class Order(models.Model):

    number = models.CharField('Номер телефонa', max_length=50)
    email = models.EmailField('Email', max_length=50, null=True, blank=True)
    note = models.TextField('Коментарии', null=True, blank=True)
    device_id = models.CharField('id of device', max_length=10, default='-1')

    def __unicode__(self):
        return self.email

    class Meta:
        verbose_name = "Заявкa"
        verbose_name_plural = "Заявки"

