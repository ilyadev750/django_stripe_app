from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название товара')
    description = models.CharField(max_length=100, unique=True, verbose_name='Описание')
    price = models.FloatField(verbose_name='Цена')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'