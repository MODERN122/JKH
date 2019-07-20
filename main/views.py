from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect


def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.mc_manager:
                return redirect('uk_lk')
            else:
                return redirect('user_lk')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})