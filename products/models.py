from django.db import models
from django.shortcuts import reverse


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


ALMACENAMIENTO_CHOICES = (
    ('16', '16 GB'),
    ('32', '32 GB'),
    ('64', '64 GB'),
    ('128', '128 GB'),
    ('256', '256 GB')
)

MEMORIA_RAM_CHOICES = (
    ('2', '2 GB'),
    ('3', '3 GB'),
    ('4', '4 GB'),
    ('6', '6 GB'),
    ('8', '8 GB'),
    ('12', '12 GB'),
    ('16', '16 GB')
)


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=15, decimal_places=0)
    image = models.ImageField(blank=True)
    brand = models.ForeignKey(Brand, models.CASCADE)
    type_product = models.ForeignKey(TypeProduct, models.CASCADE)
    color = models.ForeignKey(Color, models.SET_NULL, null=True)
    almacenamiento = models.CharField(
        choices=ALMACENAMIENTO_CHOICES, null=True, blank=True, max_length=3)
    memoria_ram = models.CharField(
        choices=MEMORIA_RAM_CHOICES, null=True, blank=True, max_length=2)
    discount_price = models.DecimalField(
        max_digits=30, decimal_places=2, null=True, blank=True)
    quantity = models.IntegerField(default=1)
    slug = models.SlugField(default="")

    description_split = []

    def get_split_description(self):
        if(len(self.description_split) == 0):
            self.description_split = self.description.split('-')
        return self.description_split
    priceString = ''

    def get_price_string(self):

        if(len(self.priceString) == 0):
            if(self.discount_price):
                self.priceString = str(self.discount_price)
            else:
                self.priceString = str(self.price)
            aux_price = ''
            count = 1
            for i in range(len(str(self.price))-1, -1, -1):
                aux_price += self.priceString[i]
                if(count % 3 == 0):
                    aux_price += '.'
                count += 1
            self.priceString = aux_price[::-1]
            if(self.priceString[0] == '.'):
                self.priceString = self.priceString[1:]
      
    def get_absolute_url(self):
        return reverse("product", kwargs={
            'slug': self.slug
        })

    def get_add_to_cart_url(self):
        return reverse("add-to-cart", kwargs={
            'slug': self.slug
        })

    def get_remove_from_cart_url(self):
        return reverse("remove-from-cart", kwargs={
            'slug': self.slug
        })

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.get_price_string()
        self.get_split_description()
        super(Product, self).save(*args, **kwargs)
