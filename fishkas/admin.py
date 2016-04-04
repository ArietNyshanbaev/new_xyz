from django.contrib import admin
from .models import Wish, Message, Best_deal, Slogan,Notifier, Imei, Image_of_Instance
# Register your models here.
admin.site.register(Wish)
admin.site.register(Message)
admin.site.register(Best_deal)
admin.site.register(Slogan)
admin.site.register(Notifier)
admin.site.register(Imei)
admin.site.register(Image_of_Instance)