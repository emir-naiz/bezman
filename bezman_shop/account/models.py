from django.db import models

# Create your models here.
class Customer(models.Model):
    full_name = models.CharField(max_length=70)
    address = models.CharField(max_length=50)
    phone = models.IntegerField()
    mail = models.EmailField()
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name="Клиент"
        verbose_name_plural="Клиенты"

# class Timetables(models.Model):
#     name = models.CharField(u'time', max_length=30)
#
#     class Meta:
#         verbose_name = 'Аккаунты'
#         verbose_name_plural = 'Аккаунты'
#
#     def __str__(self):
#         return self.name