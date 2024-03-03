from django.urls import path

from .views import buy_items, success, cancel

urlpatterns = [
    path('buy/', buy_items, name='buy'),
    path('success/', success, name='success'),
    path('cancel/', cancel, name='cancel'),
]