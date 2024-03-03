from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from items.models import Item
from .models import Cart, Order
import random
import stripe
import os
from dotenv import load_dotenv


load_dotenv()
stripe.api_key = os.getenv("API_KEY")


def add_item_to_cart(request, pk):
    try:
        order = Order.objects.get(user_session=request.session.session_key) 
    except ObjectDoesNotExist:
        order = Order()
        order.user_session = request.session.session_key
        order.number = random.randint(1,10000)
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
        cart = Cart()
        cart.item_id = Item.objects.get(pk=pk)
        cart.order_id = order
        cart.quantity = 1
        cart.total = cart.item_id.price
        cart.save()
    return redirect('get_item', pk)


def remove_item_from_cart(request, pk):
    cart = (Cart.objects.select_related('item_id')
            .select_related('order_id')
            .get(item_id__pk=pk, order_id__user_session=request.session.session_key))
    cart.quantity -= 1
    cart.total -= cart.item_id.price
    if cart.quantity == 0:
        cart.delete()
    else:
        cart.save()
    return redirect('get_item', pk)
