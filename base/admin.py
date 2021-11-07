from django.contrib import admin
from base.models import Slider, Product

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('name','title')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)