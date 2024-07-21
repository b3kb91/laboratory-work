from django.db import models
from django.urls import reverse


class Product(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name="Наименование")
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    price = models.DecimalField(max_digits=7, decimal_places=2, null=False, blank=False, verbose_name="Цена")
    image = models.URLField(null=False, blank=False, verbose_name="URL-фотка")
    remains = models.PositiveIntegerField(null=False, blank=False, verbose_name="Остаток", default=0)
    category = models.ForeignKey(
        "webapp.Category",
        on_delete=models.RESTRICT,
        verbose_name="Продукт",
        related_name="products",
    )

    def get_absolute_url(self):
        return reverse("detail", kwargs={'pk': self.pk})

    def __str__(self):
        return f"{self.title} {self.description}"

    class Meta:
        db_table = "products"
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
