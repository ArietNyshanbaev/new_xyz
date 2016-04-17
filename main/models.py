# django standart core imports
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_delete
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

class City(models.Model):
    """ City from which Instance is """

    name = models.CharField('Название города', max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "город"
        verbose_name_plural = "города"

class Instance(models.Model):
    """ Instance class which owned by Model """

    color = models.CharField('цвет', max_length=100)
    added_date = models.DateTimeField('дата добавления', default=datetime.now)
    updated_date = models.DateTimeField('дата обновления (up!)', default=datetime.now)
    telephones = models.CharField('телефон', max_length=100, null=True, blank=True)
    note = models.TextField('описание', null=True, blank=True)
    price = models.IntegerField('цена', null=True, blank=True)
    user = models.ForeignKey(User, null=True, blank=True)
    model = models.ForeignKey(Modell, verbose_name='модель')
    photo1 = models.ImageField('фото1', upload_to='media', null=True, blank=True)
    photo2 = models.ImageField('фото2', upload_to='media', null=True, blank=True)
    photo3 = models.ImageField('фото3', upload_to='media', null=True, blank=True)
    exchange = models.BooleanField('обмен', default=False)
    bargain = models.BooleanField('торг', default=False)
    guarantee = models.CharField('гарантия', max_length=100, null=True, blank=True)
    smartphone = models.BooleanField('смартфон', default=False)
    notebook = models.BooleanField('ноутбук', default=False)
    tablet = models.BooleanField('планшет', default=False)
    other = models.BooleanField('аксессуары', default=False)
    modell = models.CharField('модель', max_length='100', null=True, blank=True)
    condition = models.CharField('состояние', max_length='100', null=True, blank=True)
    documents = models.BooleanField('документы', default=False)
    box = models.BooleanField('коробка', default=False)
    earpods = models.BooleanField('наушники', default=False)
    memory = models.IntegerField('память', null=True, blank=True)
    title = models.CharField('описание темы', max_length=100, null=True, blank=True) 
    linker = models.CharField('ссылка', max_length=1000, null=True, blank=True, default='')
    city = models.ForeignKey(City, verbose_name='город', default=1)

    def save(self, *args, **kwargs):
        if self.photo1:
            try:
                img = Image.open(StringIO.StringIO(self.photo1.read()))

                if img.mode != 'RGB':
                    img = img.convert('RGB')
                img_width = self.photo1.width
                img_height = self.photo1.height
                while img_width > 1300 or img_height > 1300:
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
                background.save(output, format='JPEG', quality=70)
                output.seek(0)
                self.photo1.delete(False)
                self.photo1 = InMemoryUploadedFile(output, 'ImageField', "file.jpg", 'image/jpeg', output.len, None)
            except IOError:
                pass
        if self.photo2:
            img = Image.open(StringIO.StringIO(self.photo2.read()))
            if img.mode != 'RGB':
                img = img.convert('RGB')

            img_width = self.photo2.width
            img_height = self.photo2.height
            while img_width > 1200 or img_height > 1200:
                img_width /= 1.5
                img_height /= 1.5
            img.thumbnail((img_width, img_height), Image.ANTIALIAS)
            if img_width>img_height:
                size = (int(img_width), int(img_width*0.75))
            else:
                size = (int(img_height*1.34), int(img_height))
            image = img
            background = Image.new('RGBA', size, (255, 255, 255, 0))
            background.paste(image,((size[0] - image.size[0]) / 2, (size[1] - image.size[1]) / 2))

            output = StringIO.StringIO()
            background.save(output, format='JPEG', quality=70)
            output.seek(0)
            self.photo2.delete(False)
            self.photo2 = InMemoryUploadedFile(output, 'ImageField', "file.jpg", 'image/jpeg', output.len, None)

        if self.photo3:
            img = Image.open(StringIO.StringIO(self.photo3.read()))
            if img.mode != 'RGB':
                img = img.convert('RGB')

            img_width = self.photo3.width
            img_height = self.photo3.height
            while img_width > 1200 or img_height > 1200:
                img_width /= 1.5
                img_height /= 1.5
            img.thumbnail((img_width, img_height), Image.ANTIALIAS)
            if img_width>img_height:
                size = (int(img_width), int(img_width*0.75))
            else:
                size = (int(img_height*1.34), int(img_height))
            image = img
            background = Image.new('RGBA', size, (255, 255, 255, 0))
            background.paste(image,((size[0] - image.size[0]) / 2, (size[1] - image.size[1]) / 2))

            output = StringIO.StringIO()
            background.save(output, format='JPEG', quality=70)
            output.seek(0)
            self.photo3.delete(False)
            self.photo3 = InMemoryUploadedFile(output, 'ImageField', "file.jpg", 'image/jpeg', output.len, None)

        super(Instance, self).save(*args, **kwargs)

    def update_date(self):
        dt_now = datetime.utcnow().replace(tzinfo=utc)
        dt_new = self.updated_date
        dt = dt_now - dt_new
        minutes = ((dt.days*24*60*60) + dt.seconds) / 60
        hours = minutes / 60

        if hours >= 1:
            self.updated_date = datetime.now()
            self.save()
            status = "Тема успешно обновлена!"
            return status
        else:
            status = "Извините, обновить тему можно только 1 раз за час. Подождите еще " + str(60 - minutes) + " минут"
            return status

    def __unicode__(self):
        return unicode(self.model.title)+ ' buy ' + str(self.id)

    class Meta:
        verbose_name = "объявление"
        verbose_name_plural = "объявления"


@receiver(pre_delete, sender=Instance)
def mymodel_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.photo1.delete(False)
    instance.photo2.delete(False)
    instance.photo3.delete(False)

class Instance_buy(models.Model):
    added_date = models.DateTimeField('дата добавления', default=datetime.now)
    updated_date = models.DateTimeField('дата обновления (up!)', default=datetime.now)
    user = models.ForeignKey(User, null=True, blank=True)
    telephones = models.CharField('телефон', max_length=100, null=True, blank=True)
    price = models.IntegerField('цена', null=True, blank=True, default=-1)
    model = models.ForeignKey(Modell, verbose_name='модель')
    smartphone = models.BooleanField('смартфон', default=False)
    notebook = models.BooleanField('ноутбук', default=False)
    tablet = models.BooleanField('планшет', default=False)
    other = models.BooleanField('аксессуары', default=False)
    title = models.CharField('описание темы', max_length=100, null=True, blank=True)
    city = models.ForeignKey(City, verbose_name='город', default=1)
    note = models.TextField('описание', null=True, blank=True)
    

    def update_date(self):
        dt_now = datetime.utcnow().replace(tzinfo=utc)
        dt_new = self.updated_date
        dt = dt_now - dt_new
        minutes = ((dt.days*24*60*60) + dt.seconds) / 60
        hours = minutes / 60

        if hours >= 1:
            self.updated_date = datetime.now()
            self.save()
            status = "Тема успешно обновлена!"
            return status
        else:
            status = "Извините, обновить тему можно только 1 раз за час. Подождите еще " + str(60 - minutes) + " минут"
            return status

    def update_info(self, args):
        self.title = args['title']
        self.price = args['price']
        self.telephones = args['phone_num']
        self.note = args['note']
        self.save()
        status = 'Вы успешно отредактировали это обявление.'
        return status

    def __unicode__(self):
        return unicode(self.model.title)+ ' ' + str(self.id)

    class Meta:
        verbose_name = "объявление куплю"
        verbose_name_plural = "объявления куплю"

class Sold(models.Model):
    seller = models.ForeignKey(User, null=True, blank=True)
    date = models.DateTimeField('дата удаления', default=datetime.now)
    date_added = models.DateTimeField('дата добавления')
    price = models.IntegerField('цена', default= -1)
    model = models.ForeignKey(Modell, verbose_name='модель')
    sold_at_ibox = models.BooleanField(default=False)

    def __str__(self):
        return str(self.model) + " за " + str(self.price) + " сом " + str(self.sold_at_ibox)

    class Meta:
        verbose_name = "проданный"
        verbose_name_plural = "проданные"
