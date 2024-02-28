from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from items.models import Item
from .models import Order
import stripe
import os
from dotenv import load_dotenv


load_dotenv()
stripe.api_key = os.getenv("API_KEY")


def add_to_cart(request):
    item_id = Item.objects.get(pk=int(request.GET.get('id')))
    try:
        order = Order.objects.get(item_id=item_id, user_session=request.session.session_key)
        order.quantity += 1
        order.save()
    except ObjectDoesNotExist:
        order = Order()
        order.user_session = request.session.session_key
        order.item_id = item_id
        order.quantity = 1
        order.save()
    return redirect('get_item')


def remove_from_cart(request):
    item_id = Item.objects.get(pk=int(request.GET.get('id')))
    order = Order.objects.get(item_id=item_id, user_session=request.session.session_key)
    order.quantity -= 1
    if order.quantity == 0:
        order.delete()
    else:
        order.save()
    return redirect('get_item')

