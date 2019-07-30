from django.contrib import admin
from .models import Brand, Product, TypeProduct


@admin.register(Brand)
class Brand(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ('id', 'type_product', 'name',
                    'description', 'brand', 'price', 'color',)
