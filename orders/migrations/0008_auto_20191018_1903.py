# Generated by Django 2.2.5 on 2019-10-18 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20191018_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_method',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]
