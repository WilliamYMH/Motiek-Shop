from django.db import models


class Color(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class TypeProduct(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(blank=True)
    brand = models.ForeignKey(Brand, models.CASCADE)
    type_product = models.ForeignKey(TypeProduct, models.CASCADE)
    color = models.ForeignKey(Color, models.SET_NULL, null=True)

    def __str__(self):
        return self.name
