from django.db import models

from webapp.models import Product


class Order(models.Model):
    name = models.CharField(null=False, blank=False, max_length=100, verbose_name='Имя пользователя')
    phone = models.CharField(null=False, blank=False, max_length=100, verbose_name='Телефон')
    address = models.CharField(null=False, blank=False, max_length=100, verbose_name='Адрес')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f'{self.name}'


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.quantity}'
