from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Sum
from orders.models import Cart
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Item


def get_all_items(request):
    items = Item.objects.all()
    try:
        number_of_items = (Cart.objects.select_related('item_id')
                 .select_related('order_id')
                 .filter(order_id__user_session=request.session.session_key)
                 .aggregate(Sum('quantity')))
        total_sum = (Cart.objects.select_related('item_id')
                 .select_related('order_id')
                 .filter(order_id__user_session=request.session.session_key)
                 .aggregate(Sum('total')))
    except ObjectDoesNotExist:
        number_of_items = None
    context = {'items': items,
               'number_of_items': number_of_items['quantity__sum'],
               'total_sum': total_sum['total__sum']}
    return render(request, 'items/get_all_items.html', context)


def get_item(request, pk):
    try:
        cart = (Cart.objects.select_related('item_id')
                 .select_related('order_id')
                 .get(item_id__pk=pk, 
                      order_id__user_session=request.session.session_key))
        item = cart.item_id
    except ObjectDoesNotExist:
        cart = None
        item = Item.objects.get(pk=pk)
    context = {'item': item, 
               'cart': cart}
    return render(request, 'items/item.html', context)



    



