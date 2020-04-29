from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePayment
from django.conf import settings
from comms.models import order
import stripe
# Create your views here.

stripe.api_key = settings.STRIPE_SECRET


@login_required()
def payment(request):
    if request.method == "POST":
        payment_form = MakePayment(request.POST)
        this_order = order(request.POST)

        if payment_form.is_valid():
            total = this_order.price

            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="GBP",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(
                    request, "Card declined, Unable to take payment from this card")
            if customer.paid:
                messages.error(request, "Payment taken successfully")
                return redirect(reverse('profile'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(request, "Unable to take a payment with that card")
    else:
        payment_form = MakePayment()
    return render(request, "payment.html", {"payment_form": payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})
