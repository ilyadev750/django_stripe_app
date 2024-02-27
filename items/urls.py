from django.urls import path
from .views import get_all_items, get_item, buy_item,  success, cancel

urlpatterns = [
    path('', get_all_items, name='get_all_items'),
    path('item/', get_item, name='get_item'),
    path('buy/', buy_item, name='buy_item'),
    path('success/', success, name='success'),
    path('cancel/', cancel, name='cancel'),
]
