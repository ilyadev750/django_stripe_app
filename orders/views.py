from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from items.models import Item
from .models import Cart, Order
import stripe
import os
from dotenv import load_dotenv


load_dotenv()
stripe.api_key = os.getenv("API_KEY")


def add_item_to_cart(request):
    pk=int(request.GET.get('id'))
    try:
        cart = (Cart.objects.select_related('item_id')
                .select_related('order_id')
                .get(item_id__pk=pk,
                     order_id__user_session=request.session.session_key))
        cart.quantity += 1
        cart.save()
    except ObjectDoesNotExist:
        new_order = Order()
        new_order.user_session = request.session.session_key
        new_order.number += 1
        new_order.save()
        cart = Cart()
        cart.item_id = Item.objects.get(pk=pk)
        cart.order_id = new_order
        cart.quantity = 1
        cart.save()
    return redirect('get_item', pk)


def remove_item_from_cart(request):
    pass
    pk = int(request.GET.get('id'))
    cart = (Cart.objects.select_related('item_id')
            .select_related('order_id')
            .get(item_id__pk=pk, order_id__user_session=request.session.session_key))
    cart.quantity -= 1
    if cart.quantity == 0:
        cart.delete()
    else:
        cart.save()
    return redirect('get_item', pk)
