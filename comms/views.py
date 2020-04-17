from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from comms.forms import ContactForm

# Create your views here.


@login_required
def contact(request):
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
    else:
        contact_form = ContactForm()
    return render(request, 'contact.html', {'contact_form': contact_form})
