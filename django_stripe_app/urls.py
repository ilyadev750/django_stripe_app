from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('items.urls')),
    path('', include('orders.urls')),
    path('', include('stripe_api.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
]
