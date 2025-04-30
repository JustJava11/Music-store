from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from profiles.models import UserProfile
from products.models import Product
from profiles.forms import UserRegisterForm, UserChangeForm, ProfileForm


def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')

    else:
        form = UserRegisterForm()

    return render(request, 'profiles/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(reverse_lazy('profile', kwargs={'pk': user.pk}))

    else:
        form = AuthenticationForm()
    return render(request, 'profiles/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def profile_detail(request, pk):
    profile = get_object_or_404(UserProfile, user__pk=pk)

    products = Product.objects.filter(user=profile.user)
    product_count = products.count()

    return render(
        request,
        'profiles/profile_detail.html',
        {
            'title': f'Профиль пользователя {profile.user.username} - Music Store',
            'profile': profile,
            'products': products,
            'product_count': product_count,
        }
    )


@login_required
def update_profile(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('profile', pk=request.user.pk)
    else:
        profile_form = ProfileForm(instance=profile)

    return render(
        request,
        'profiles/profile_form.html',
        {
            'title': 'Music Store',
            'profile_form': profile_form,
        }
    )

@login_required
def update_user(request):
    user = request.user
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance = user)
        if form.is_valid():
            form.save()
            return redirect('profile', request.user.pk)
    else:
        form = UserChangeForm(instance=user)
    return render(
        request,
        'profiles/update_user.html',
        {
            'title': 'Music Store',
            'form': form
        }
    )
