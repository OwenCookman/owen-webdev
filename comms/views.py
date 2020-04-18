from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from comms.forms import ContactForm

# Create your views here.


@login_required
def contact(request):
    if request.method == "POST":
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            contact_form.save()

            query = auth.authenticate(website=request.POST['website'],
                                      functionality=request.POST['functionality'],
                                      url=request.POST['url'],
                                      business=request.POST['business'],
                                      customer=request.POST['customer'],
                                      message=request.POST['message'])
        else:
            messages.error(
                request, "Sorry, your request could not be submitted, please try again")
    else:
        contact_form = ContactForm()
    return render(request, 'contact.html', {'contact_form': contact_form})
