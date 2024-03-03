from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist
from .utils import create_order, create_new_cart
from .models import Cart, Order


def add_item_to_cart(request, pk):
    """Добавить товар в корзину"""
    try:
        order = Order.objects.get(user_session=request.session.session_key)
    except ObjectDoesNotExist:
        order = create_order(request=request)
        order.save()
    try:
        cart = (Cart.objects.select_related('item_id')
                .select_related('order_id')
                .get(item_id__pk=pk,
                     order_id__user_session=request.session.session_key))
        cart.quantity += 1
        cart.total += cart.item_id.price
        cart.save()
    except ObjectDoesNotExist:
        cart = create_new_cart(pk=pk, order=order)
        cart.save()
    return redirect('get_item', pk)


def remove_item_from_cart(request, pk):
    """Удалить товар из корзины"""
    cart = (Cart.objects.select_related('item_id')
            .select_related('order_id')
            .get(item_id__pk=pk,
                 order_id__user_session=request.session.session_key))
    cart.quantity -= 1
    cart.total -= cart.item_id.price
    if cart.quantity == 0:
        cart.delete()
    else:
        cart.save()
    return redirect('get_item', pk)
