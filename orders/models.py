from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product
from django.conf import settings





class Departments(models.Model):
    name = models.CharField(max_length=255, default='')


class Citys(models.Model):
    name = models.CharField(max_length=255, default='')
    state = models.IntegerField()
    department = models.ForeignKey(Departments, models.CASCADE)

    def __str__(self):
        return (self.name)


class ShippingAddress(models.Model):
    user = models.ForeignKey(get_user_model(), models.CASCADE)
    address = models.CharField(max_length=250)
    city = models.ForeignKey(Citys, models.SET_NULL, null=True)
    codigo_postal = models.CharField(max_length=30)
    number_telephone = models.CharField(max_length=30)
    is_default = models.BooleanField(default=False)

    def __str__(self):
        return '%s %s' % (self.user, self.address)


"""
class ShoppingCart(models.Model):
    user = models.ForeignKey(User, models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.user, self.product)


class Product_ShoppingCart(models.Model):
    product = models.ForeignKey(Product, models.CASCADE)
    shoppingCart = models.ForeignKey(ShoppingCart, models.CASCADE)
    quantity = models.IntegerField()
"""


class Coupon(models.Model):
    code = models.CharField(max_length=15)
    amount = models.FloatField()

    def __str__(self):
        return self.code


class OrderProduct(models.Model):
    user = models.ForeignKey(get_user_model(), models.CASCADE)
    product = models.ForeignKey(Product, models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return '%s' % self.user

    def get_total_price(self):
        return self.quantity*self.product.price

    def get_total_discount(self):
        return self.quantity*self.product.discount_price

    def get_ammount_saved(self):
        return self.get_total_price() - self.get_total_discount()

    def get_final_price(self):
        if(self.product.discount_price):
            return self.get_total_discount()
        return self.get_total_price()


class Order(models.Model):

    user = models.ForeignKey(get_user_model(), models.CASCADE)
    payment_method = models.CharField(max_length=255, default='', null=True, blank=True)
    ordered_date = models.DateTimeField(null=True, blank=True)
    #total = models.DecimalField(max_digits=30, decimal_places=2)
    coupon = models.ForeignKey(Coupon, models.SET_NULL, null=True, blank=True)
    products = models.ManyToManyField(OrderProduct)
    refund_requested = models.BooleanField(default=False)
    refund_granted = models.BooleanField(default=False)
    received = models.BooleanField(default=False)
    ordered = models.BooleanField(default=False)
    use_default_shipping_address = models.BooleanField(default=False)
    shipping_address = models.ForeignKey(
        ShippingAddress, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.user.username

    def get_total(self):
        total = 0
        for i in self.products.all():
            total += i.get_final_price()
        if(self.coupon):
            total -= self.coupon.amount
        return total


class Refund(models.Model):
    order = models.ForeignKey(Order, models.CASCADE)
    reason = models.TextField
    accepted = models.BooleanField(default=False)
    email = models.EmailField

    def __str__(self):
        return self.pk
