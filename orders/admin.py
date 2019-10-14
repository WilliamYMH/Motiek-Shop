from django.contrib import admin
from .models import PaymentMethod, Citys, Departments, ShippingAddress, Order
# Register your models here.
admin.site.register(PaymentMethod)
admin.site.register(Citys)
admin.site.register(Departments)
admin.site.register(ShippingAddress)
admin.site.register(Order)