# Generated by Django 3.1.3 on 2020-12-03 04:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_customer_image'),
        ('supershop', '0005_auto_20201202_1012'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.customer'),
        ),
    ]
