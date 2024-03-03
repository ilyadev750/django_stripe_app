from django.core.exceptions import ObjectDoesNotExist
from orders.models import Cart
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Item


def get_all_items(request):
    items = Item.objects.all()
    context = {'items': items}
    return render(request, 'items/get_all_items.html', context)


def get_item(request, pk):
    try:
        order = (Cart.objects.select_related('item_id')
                 .select_related('order_id')
                 .get(item_id__pk=pk, 
                      order_id__user_session=request.session.session_key))
        item = order.item_id
    except ObjectDoesNotExist:
        order = None
        item = Item.objects.get(pk=pk)
    buy_url = reverse('buy_item')
    add_item = reverse('add_item')
    remove_item = reverse('remove_item')
    context = {'item': item, 
               'buy_url': buy_url,
               'add_item': add_item,
               'remove_item': remove_item,
               'order': order}
    return render(request, 'items/item.html', context)



    



