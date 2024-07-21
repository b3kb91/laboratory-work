from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name="Наименование", unique=True)
    description = models.TextField(max_length=50, null=True, blank=True, verbose_name="Описание")

    def get_absolute_url(self):
        return reverse("detail", kwargs={'pk': self.pk})

    def __str__(self):
        return f"{self.title} {self.description}"

    class Meta:
        db_table = 'categories'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'