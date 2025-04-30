from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Order, OrderItem
from .forms import OrderItemForm

from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Order, OrderItem
from .forms import OrderItemForm
from django.contrib.auth.decorators import login_required


@login_required
def create_order_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = OrderItemForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']

            if product.quantity < quantity:
                form.add_error('quantity', 'Not enough stock available.')
            else:
                order = Order.objects.create(user=request.user)
                order_item = OrderItem(
                    order=order,
                    product=product,
                    quantity=quantity,
                    price=product.price
                )
                order_item.save()

                product.quantity -= quantity
                product.save()

                return redirect('order_success')
    else:
        form = OrderItemForm()

    return render(request, 'orders/create_order.html', {'form': form, 'product': product})


@login_required
def user_orders_view(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/user_orders.html', {'orders': orders})

@login_required
def order_success_view(request):
    return render(request, 'orders/success.html')


@login_required
def user_orders_view(request):
    orders = Order.objects.filter(user=request.user)

    return render(request, 'orders/user_orders.html', {'orders': orders})
