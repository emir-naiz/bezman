# Generated by Django 3.1.3 on 2020-12-04 05:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_customer_mail'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': 'Клиент', 'verbose_name_plural': 'Клиенты'},
        ),
    ]
