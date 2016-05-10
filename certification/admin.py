from django.contrib import admin
from .models import CertifiedDevice, Photo, Modell, Category, Brand, Order

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Modell)
admin.site.register(Order)

class CertifiedDeviceAdmin(admin.ModelAdmin):
	list_display = ('user', 'created_date', 'price')
	list_filter = ('created_date', 'price')
admin.site.register(CertifiedDevice, CertifiedDeviceAdmin)

class PhotoAdmin(admin.ModelAdmin):
	list_display = ('device',)
	list_filter = ('device',)
admin.site.register(Photo, PhotoAdmin)

