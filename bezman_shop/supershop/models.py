from django.db import models
from account.models import Customer
import django_filters
# Create your models here.
class Product(models.Model):
    types = (
        ('classic', 'classic'),
        ('sport', 'sport'),
        ('dm', 'demi-season'),
        ('winter', 'winter')
    )
    genders = (
        ('male', 'male'),
        ('female', 'female'),
        ('uni', 'uni')
    )
    sizes = (
        ('child', 'child'),
        ('medium', 'medium'),
        ('large', 'large'),
        ('XL', 'XL')
    )
    name = models.CharField(max_length=40)
    product_type = models.CharField(max_length=40, choices=types)
    gender = models.CharField(max_length=20, choices=genders)
    product_model = models.CharField(max_length=50)
    price = models.IntegerField()
    manufacturer = models.CharField(max_length=15)
    size = models.CharField(max_length=20, choices=sizes)
    image = models.ImageField(blank=True, default='default.jpeg')  # blank=True означает изображение не обязательно

    def __str__(self):
        return self.name + ' ' + self.product_model

    class Meta:
        verbose_name="Товар"
        verbose_name_plural="Товары"


class Order(models.Model):
    statuses = (
        ('Not delivered', 'Not delivered'),
        ('In process', 'In process'),
        ('Delivered', 'Delivered')
    )
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=statuses, default='New order')
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.product.name + ' ' + self.status

    class Meta:
        verbose_name="Заказ" # при помощи этого меняем язык
        verbose_name_plural="Заказы" # при помощи этого меняем язык

