# Generated by Django 3.1.3 on 2020-12-09 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20201209_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='image',
            field=models.ImageField(blank='True', default='anonymous.png', upload_to=''),
        ),
    ]
