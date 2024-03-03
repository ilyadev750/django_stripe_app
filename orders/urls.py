from django.urls import path
from .views import add_item_to_cart, remove_item_from_cart

urlpatterns = [
    path('add_item/', add_item_to_cart, name='add_item'),
    path('remove_item/', remove_item_from_cart, name='remove_item'),
    # path('item/', get_item, name='get_item'),
    # path('buy/', buy_item, name='buy_item'),
    # path('success/', success, name='success'),
    # path('cancel/', cancel, name='cancel'),
]