from django.db import models

class Snacks(models.Model): 
    class CurrencyChoice(models.TextChoices):
        som = "C"
        dollar = "$"
    title = models.CharField(
        max_length=255, verbose_name="Название"
    )
    image = models.ImageField(
        upload_to="products", verbose_name="Картинка"
    )
    description = models.TextField(
        verbose_name="Описание", default=("No description available")
    )
    price = models.IntegerField(
        default=0, verbose_name="Цена"
    )
    currency = models.CharField(
        max_length=100, choices=CurrencyChoice.choices,
        default=CurrencyChoice.dollar, verbose_name="Валюта"
    )
    is_active = models.BooleanField(
        default=True, verbose_name="Активный"
    )

    class Meta:
        verbose_name = "Закуска"
        verbose_name_plural = "Закуски"

    def __str__(self):
        return self.title