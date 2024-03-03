from .models import Cart, Order
from items.models import Item
import random


def create_order(request):
    """Создать заказ для уникального пользователя"""
    order = Order()
    order.user_session = request.session.session_key
    order.number = random.randint(1, 10000)
    return order


def create_new_cart(pk, order):
    """Создать корзину для добавляемого товара"""
    cart = Cart()
    cart.item_id = Item.objects.get(pk=pk)
    cart.order_id = order
    cart.quantity = 1
    cart.total = cart.item_id.price
    return cart
