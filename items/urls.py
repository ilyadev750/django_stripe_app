from django.urls import path
from .views import get_all_items, get_item

urlpatterns = [
    path('', get_all_items, name='get_all_items'),
    path('item/<int:pk>', get_item, name='get_item'),
]
