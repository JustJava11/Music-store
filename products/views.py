from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse
from .models import Product
from .forms import ProductForm


def superuser_required(view_func):
    return user_passes_test(lambda u: u.is_superuser)(view_func)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})


@superuser_required
def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect('main_page')
    else:
        form = ProductForm()

    return render(request, "products/product_form.html", {"form": form})


@superuser_required
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect(reverse('product_detail', args=[product.pk]))
    return render(request, 'products/product_form.html', {'form': form, 'product': product})


@superuser_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('main_page')
    return render(request, 'products/product_confirm_delete.html', {'product': product})
