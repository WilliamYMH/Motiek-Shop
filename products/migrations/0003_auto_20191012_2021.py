# Generated by Django 2.2.5 on 2019-10-12 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_discount_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(),
        ),
    ]
