# Generated by Django 3.1.3 on 2020-12-09 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20201204_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='image',
            field=models.ImageField(default='123.jpg', upload_to=''),
        ),
    ]
