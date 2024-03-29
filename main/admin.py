from django.contrib import admin
from .models import Category, Instance, Brand, Modell, Sold, City, Instance_buy, Device
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class InstanceAdmin(admin.ModelAdmin):
	list_display = ('user', 'added_date', 'price')
	list_filter = ('added_date', 'price')
admin.site.register(Instance, InstanceAdmin)

class Instance_buy_Admin(admin.ModelAdmin):
	list_display = ('user', 'added_date', 'min_price', 'max_price')
	list_filter = ('added_date', 'min_price',  'max_price')
admin.site.register(Instance_buy, Instance_buy_Admin)

class SoldAdmin(admin.ModelAdmin):
	list_display = ('seller', 'price', 'date', 'sold_at_ibox')
	list_filter = ('date', 'price', 'sold_at_ibox')

admin.site.register(Sold, SoldAdmin)
# Register your models here.
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Modell)
admin.site.register(City)
admin.site.register(Device)

# customizng of user admin django
UserAdmin.list_display = ('email', 'first_name', 'last_name', 'is_active', 'date_joined', 'is_staff')
UserAdmin.list_filter = ('is_active', 'date_joined', 'is_staff', 'last_login')
admin.site.unregister(User)
admin.site.register(User, UserAdmin)