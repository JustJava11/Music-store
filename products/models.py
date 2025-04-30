from django.db import models
from categories.models import Category
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField(max_length=256, verbose_name='product title')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='product price')
    description = models.TextField(null=True, blank=True, verbose_name='product description')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='product created time')
    product_image = models.ImageField(upload_to='images/product_images', verbose_name='product image')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products', verbose_name='categories')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products', verbose_name='user')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Available quantity')

    def __str__(self):
        return self.title