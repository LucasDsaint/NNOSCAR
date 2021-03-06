# Generated by Django 3.1.6 on 2021-03-09 10:38

from django.db import migrations, models
import oscar.core.utils


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0006_auto_20200724_0909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockrecord',
            name='price',
            field=models.CharField(blank=True, default=0, max_length=12, null=True, verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='stockrecord',
            name='price_currency',
            field=models.CharField(blank=True, default=oscar.core.utils.get_default_currency, max_length=12, null=True, verbose_name='Currency'),
        ),
    ]
