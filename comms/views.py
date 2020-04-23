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
            print("is valid")
            contact_form.cleaned_data(
                business_name=request.POST['business_name'])
            contact_form.cleaned_data(website=request.POST['website'])
            contact_form.cleaned_data(functionality=request.POST['functionality'])
            contact_form.cleaned_data(url=request.POST['url'])
            contact_form.cleaned_data(business_type=request.POST['business_type'])
            contact_form.cleaned_data(customer=request.POST['customer'])
            contact_form.cleaned_data(message=request.POST['message'])
            contact_form.cleaned_data(date=request.POST['date'])
            contact = contact_form.save(commit=False)
            contact.client = request.User
            contact.save()
        else:
            messages.error(
                request, "Sorry, your request could not be submitted, please try again")
    else:
        print("failed")
        contact_form = forms.ContactForm()
    return render(request, 'contact.html', {'contact_form': contact_form})
