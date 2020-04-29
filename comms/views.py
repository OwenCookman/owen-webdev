from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.contrib import messages
from . import forms
import os

# Create your views here.

MY_EMAIL = os.environ.get('MY_EMAIL')

@login_required
def contact(request):
    if request.method == "POST":
        contact_form = forms.ContactForm(request.POST)

        if contact_form.is_valid():
            contact = contact_form.save(commit=False)
            contact.client = request.user
            contact.save()
            messages.success(request, "Your form submitted successfully")
            message = contact_form.cleaned_data['message']
            subject = "order"
            from_email = request.user.email

            email = EmailMessage(subject, message, from_email, to=['MY_EMAIL'])
            email.send()

            return redirect('profile')

        else:
            messages.error(
                request, "Sorry, your request could not be submitted, please try again")

    else:
        print("failed")
        contact_form = forms.ContactForm()
    return render(request, 'contact.html', {'contact_form': contact_form})
