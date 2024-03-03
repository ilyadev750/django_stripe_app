from django.urls import path
from .views import add_item_to_cart, remove_item_from_cart

urlpatterns = [
    path('add_item/<int:pk>/', add_item_to_cart, name='add_item'),
    path('remove_item/<int:pk>/', remove_item_from_cart, name='remove_item'),
]
