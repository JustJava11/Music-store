from django.contrib.auth import login
from django.shortcuts import render, redirect
from profiles.forms import UserRegisterForm

def register(request):
    if request == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('category_list')
    else:
        form = UserRegisterForm()
    return render(request, 'app/register.html', {'title': 'Guitar store', 'form': form})

