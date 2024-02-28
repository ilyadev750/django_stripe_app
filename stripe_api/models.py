from django.db import models
from items.models import Item

class Order(models.Model):
    user_session = models.CharField(max_length=100, verbose_name='Номер сессии')
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name='Товар')
    quantity = models.IntegerField(verbose_name='Количество товара')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'