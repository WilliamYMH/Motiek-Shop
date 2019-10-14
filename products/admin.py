from django.contrib import admin
from .models import Brand, Product, TypeProduct, Color


admin.site.register(TypeProduct)
admin.site.register(Color)


@admin.register(Brand)
class Brand(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Product)
class Product(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('id', 'type_product', 'name',
                    'brand', 'price', 'quantity', 'color', 'slug')
