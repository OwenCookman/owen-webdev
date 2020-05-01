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
def summary(request, slug):
    this_order = order.objects.get(id=slug)
    to_pay = this_order.price / 2
    context = {'this_order': this_order, "to_pay": to_pay}
    return render(request, "summary.html", context)


@login_required()
def payment(request, slug):
    this_order = order.objects.get(id=slug)
    to_pay = this_order.price / 2

    if request.method == "POST":
        payment_form = MakePayment(request.POST)
        print(payment_form)

        if payment_form.is_valid():

            try:
                customer = stripe.Charge.create(
                    amount=int(to_pay * 100),
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
            messages.error(request, "Unable to take a payment with that card")
    else:
        payment_form = MakePayment()

    context = {'payment_form': payment_form,
               'publishable': settings.STRIPE_PUBLISHABLE,
               'this_order': this_order,
               'to_pay': to_pay}
    return render(request, "payment.html", context)
