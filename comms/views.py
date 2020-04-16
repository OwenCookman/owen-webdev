from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from comms.forms import ContactForm

# Create your views here.

@login_required
def contact(request):
    return render(request, 'contact.html')