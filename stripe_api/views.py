import stripe
import os
from orders.models import Order
from dotenv import load_dotenv
from django.shortcuts import redirect, render
from django_stripe_app.settings import DOMAIN
from orders.models import Cart

load_dotenv()
stripe.api_key = os.getenv("API_KEY")


def buy_items(request):
    """Покупка товаров, взаимодействие со Stripe API"""
    line_items = []
    items = (Cart.objects.select_related('item_id')
             .select_related('order_id')
             .filter(order_id__user_session=request.session.session_key))
    if request.method == "POST":
        for item in items:
            line_items.append({'price': item.item_id.price_id,
                               'quantity': item.quantity})
        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=line_items,
                mode='payment',
                success_url=DOMAIN + 'success',
                cancel_url=DOMAIN + 'cancel',
            )
        except Exception as e:
            return e
        return redirect(checkout_session.url, code=303)


def success(request):
    """Рендеринг страницы успешного платежа"""
    order = Order.objects.get(user_session=request.session.session_key)
    order.delete()
    return render(request, 'items/success.html')


def cancel(request):
    """Рендеринг страницы отмены платежа"""
    return render(request, 'items/cancel.html')
