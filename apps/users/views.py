from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect

from .forms import SignupUserForm


def signup_view(request):
    user_form = SignupUserForm(request.POST or None)
    if user_form.is_valid():
        user = user_form.save(commit=False)
        password = user.password
        user.password = make_password(password)
        user.save()
        user = authenticate(username=user.username, password=password)
        login(request, user)
        return redirect('contacts')
    else:
        return render(request, 'users/signup.html', {'form': user_form})
