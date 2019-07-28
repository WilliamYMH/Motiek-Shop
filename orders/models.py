from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class PaymetMethod(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Departments(models.Model):
    name = models.CharField(max_length=255, default='')


class Citys(models.Model):
    name = models.CharField(max_length=255, default='')
    state = models.IntegerField()
    department = models.ForeignKey(Departments, models.CASCADE)


class ShippingAddress(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
    address = models.CharField(max_length=250)
    department = models.ForeignKey(Departments, models.SET_NULL, null=True)
    city = models.ForeignKey(Citys, models.SET_NULL, null=True)
    codigo_postal = models.CharField(max_length=30)
    number_telephone = models.CharField(max_length=30)

    def __str__(self):
        return '%s %s' % (self.user, self.address)


class ShoppingCart(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    product = models.ForeignKey(Product, models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return '%s %s' % (self.user, self.product)


class Order(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    paymet_method = models.ForeignKey(PaymetMethod, models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.user


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, models.CASCADE)
    product = models.ForeignKey(Product, models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return '%s %s' % (self.order, self.product)
