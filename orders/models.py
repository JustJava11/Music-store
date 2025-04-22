from django.db import models
from profiles.models import UserProfile
from products.models import Product

class Order(models.Model):
    customer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='order customer')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created date')
    products = models.ManyToManyField(Product, through='OrderItem', verbose_name='products')

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='orders')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='products')
    order_image = models.ImageField(upload_to='images/order_images')
    quantity = models.PositiveIntegerField(verbose_name='quantity')
    price_at_purchase = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='price at purchase')
