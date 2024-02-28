import stripe
import os
from django.core.exceptions import ObjectDoesNotExist
from dotenv import load_dotenv
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Item
from stripe_api.models import Order
from django_stripe_app.settings import DOMAIN


load_dotenv()
stripe.api_key = os.getenv("API_KEY")


def get_all_items(request):
    items = Item.objects.all()
    item_url = reverse('get_item')
    context = {'items': items, 'item_url': item_url}
    return render(request, 'items/get_all_items.html', context)


def get_item(request):
    item = Item.objects.get(pk=int(request.GET.get('id')))
    try:
        order = Order.objects.get(item_id=item, user_session=request.session.session_key)
        quantity = order.quantity
    except ObjectDoesNotExist:
        quantity = 0
    buy_url = reverse('buy_item')
    add_item = reverse('add_item')
    remove_item = reverse('remove_item')
    context = {'item': item, 
               'buy_url': buy_url,
               'add_item': add_item,
               'remove_item': remove_item,
               'quantity': quantity}
    return render(request, 'items/item.html', context)



    


# def byu_all(request):
#     line_items = []
#     items = Item.objects.all()
#     if request.method == "POST":
#         for item in items:
#             line_items.append({'price': item.price_id,
#                                'quantity': 1})
#         try:
#             checkout_session = stripe.checkout.Session.create(
#                 line_items=line_items,
#                 mode='payment',
#                 success_url=DOMAIN + 'success',
#                 cancel_url=DOMAIN + 'cancel',
#             )
#         except Exception as e:
#             return e
#         return redirect(checkout_session.url, code=303)


def buy_item(request):
    item = Item.objects.get(pk=int(request.GET.get('id')))
    if request.method == "POST":
        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                {
                    'price': item.price_id,
                    'quantity': 1,
                },
            ],
                mode='payment',
                success_url=DOMAIN + 'success',
                cancel_url=DOMAIN + 'cancel',
            )
        except Exception as e:
            return e
        return redirect(checkout_session.url, code=303)

def success(request):
    return render(request, 'items/success.html')


def cancel(request):
    return render(request, 'items/cancel.html')