from django.db import models
from categories.models import Category
from profiles.models import UserProfile

class Tag(models.Model):
    title = models.CharField(max_length=256, verbose_name='tag title')

class Product(models.Model):
    title = models.CharField(max_length=256, verbose_name='product title')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='product price')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    seller = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
