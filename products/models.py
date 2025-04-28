from django.db import models
from categories.models import Category
from profiles.models import UserProfile

class Product(models.Model):
    title = models.CharField(max_length=256, verbose_name='product title')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='product price')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='category created time')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
    seller = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class ProductGallery(models.Model):
    image = models.ImageField(upload_to='images/product_images', verbose_name='product image', null=True, blank=True)

    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Product')

    def __str__(self):
        return f"{self.product.title} - {self.pk}"

    class Meta:
        verbose_name_plural = 'Gallery'
