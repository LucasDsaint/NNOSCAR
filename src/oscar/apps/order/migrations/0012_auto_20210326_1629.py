# Generated by Django 3.1.6 on 2021-03-26 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0011_auto_20200801_0817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billingaddress',
            name='line2',
            field=models.DateField(verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='line2',
            field=models.DateField(verbose_name='Data'),
        ),
    ]
