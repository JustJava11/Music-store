from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from decimal import Decimal

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.product.title}"

    def get_total_price(self):
        return self.price * self.quantity

    def save(self, *args, **kwargs):
        if self.price is None or self.price == Decimal('0.00'):
            self.price = self.product.price
        super().save(*args, **kwargs)
