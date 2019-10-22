from django.contrib import admin
from .models import Citys, Departments, ShippingAddress, Order
# Register your models here.
admin.site.register(Citys)
admin.site.register(Departments)
admin.site.register(ShippingAddress)
admin.site.register(Order)