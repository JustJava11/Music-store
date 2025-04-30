from django.shortcuts import render
from products.models import Product

def main_page(request):
    products = Product.objects.all().order_by('-created_at')
    new_products = Product.objects.order_by('-created_at')[:8]
    return render(request, 'main_page_app/main.html', {
        'products': products,
        'new_products': new_products
    })