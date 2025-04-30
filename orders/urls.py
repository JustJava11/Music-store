from django.urls import path
from orders.views import create_order_view, order_success_view, user_orders_view

urlpatterns = [
    path('create/<int:product_id>/', create_order_view, name='create_order'),
    path('success/', order_success_view, name='order_success'),
    path('my-orders/', user_orders_view, name='user_orders'),
]
