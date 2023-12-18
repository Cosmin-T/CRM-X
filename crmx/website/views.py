from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    # Check login
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenthicate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Authentication successful!")
            return redirect ('home')
        else:
            messages.success(request, "Authentication failed, try again.")
            return redirect ('home')
    else:
        return render(request, 'home.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "Logout successful!")
    return redirect ('home')

def register_user(request):
    return render(request, 'register.html', {})