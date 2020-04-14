from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required

# Create your views here.


def portfolio(request):
    """Returns the portfolio.html file"""
    return render(request, 'portfolio.html')
