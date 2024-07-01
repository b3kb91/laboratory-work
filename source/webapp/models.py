from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name="Наименование", unique=True)
    description = models.CharField(max_length=50, null=True, blank=True, verbose_name="Описание")

    def __str__(self):
        return f"{self.title} {self.description}"

    class Meta:
        db_table = 'categories'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name="Наименование")
    description = models.CharField(max_length=50, null=True, blank=True, verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    price = models.DecimalField(max_digits=7, decimal_places=2, null=False, blank=False)
    image = models.URLField(null=False, blank=False)
    category = models.ForeignKey(
        "webapp.Category",
        on_delete=models.RESTRICT,
        verbose_name="Продукт",
        related_name="products",
    )

    def __str__(self):
        return f"{self.title} {self.description}"

    class Meta:
        db_table = "products"
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
