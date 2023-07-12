from django.contrib import admin
from .models import *

# class CatagoryAdmin(admin.ModelAdmin):
#     list_display=('name','description') 
# class ProductAdmin(admin.ModelAdmin):
#     list_display=('name','quantity')


# Register your models here.
admin.site.register(Catagory)
admin.site.register(Products)
admin.site.register(Bag)
admin.site.register(Favourite)