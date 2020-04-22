from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from . import forms

# Create your views here.


@login_required
def contact(request):
    if request.method == "POST":
        contact_form = forms.ContactForm(request.POST)

        if contact_form.is_valid():
            contact = contact_form.save(commit=False)
            contact.client = request.User
            contact.save()
        else:
            messages.error(
                request, "Sorry, your request could not be submitted, please try again")
    else:
        contact_form = forms.ContactForm()
    return render(request, 'contact.html', {'contact_form': contact_form})
