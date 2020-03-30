from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages

# Create your views here.

def index(request):
    """Returns the index.html file"""
    return render(request, 'index.html')

def logout(request):
    """Logs the user out"""
    auth.logout(request)
    messages.success(request, "You have been logged out successfully")
    return redirect(reverse('index'))

def Login(request):
    """Returns the login page"""
    return render(request, 'login.html')


