from django.db import models
from django.urls import reverse


class Basket(models.Model):
    product = models.ForeignKey('webapp.Product', on_delete=models.CASCADE,
                                verbose_name="Продукт",
                                related_name="baskets", )
    quantity = models.PositiveIntegerField(verbose_name='Количество', default=1)

    def get_absolute_url(self):
        return reverse("detail", kwargs={'pk': self.pk})

    def total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.quantity}"

    class Meta:
        db_table = "baskets"
        verbose_name = "Товар в корзине"
        verbose_name_plural = "Товары в корзине"
