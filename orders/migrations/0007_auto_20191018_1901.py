# Generated by Django 2.2.5 on 2019-10-18 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_order_shipping_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='use_default_shipping_address',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='is_default',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_method',
            field=models.CharField(default='', max_length=255),
        ),
    ]
