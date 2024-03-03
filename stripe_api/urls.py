from django.urls import path

# from .views import add_to_cart, remove_from_cart

urlpatterns = [
    path('buy/<int:order_id>', ),
    path('buy/', buy_item, name='buy_item'),
    path('success/', success, name='success'),
    path('cancel/', cancel, name='cancel'),
]