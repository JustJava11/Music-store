from django.urls import path
from products.views import *

urlpatterns = [
    path('<int:pk>/', product_detail, name='product_detail'),
    path('create/', product_create, name='product_create'),
    path('<int:pk>/edit/', product_update, name='product_update'),
    path('<int:pk>/delete/', product_delete, name='product_delete'),
]
