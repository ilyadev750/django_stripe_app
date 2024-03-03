from django.db import models
from items.models import Item

class Order(models.Model):
    user_session = models.CharField(default=None, max_length=100, verbose_name='Номер сессии')
    number = models.IntegerField(default=0, verbose_name='Номер заказа')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self) -> str:
        return f'Заказ № {self.pk}' 

class Cart(models.Model):
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name='Товар')
    quantity = models.IntegerField(default=0, verbose_name='Количество товара')
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE,
                                 verbose_name='Номер заказа',
                                 default=None)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self) -> str:
        return f'Заказ № {self.order_id} - {self.item_id}'
    
