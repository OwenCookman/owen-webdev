from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from .forms import MakePayment
from comms.models import order
from .models import invoice
from django.contrib.auth.models import User
import stripe
# Create your views here.

stripe.api_key = settings.STRIPE_SECRET


@login_required()
def user_invoice(request, slug):
    user = User.objects.get(email=request.user.email)
    this_invoice = invoice.objects.get(id=slug)
    context = {'user': user, 'this_invoice': this_invoice}
    return render(request, 'invoice.html', context)


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
                new_invoice = invoice()
                new_invoice.business_name = this_order.business_name
                new_invoice.start_date = this_order.date
                new_invoice.card_type = customer.payment_method_details.card.brand
                new_invoice.last4 = customer.payment_method_details.card.last4
                new_invoice.amount_charged = to_pay
                new_invoice.stripe_receipt = customer.receipt_url
                new_invoice.client = this_order.client
                if this_order.deposit_paid:
                    new_invoice.remaining_cost = 0
                    new_invoice.description = "Payment for completed website build"
                else:
                    new_invoice.remaining_cost = to_pay
                    new_invoice.description = "Deposit payment to begin website build"
                new_invoice.save()

                messages.success(request, "Payment taken successfully")
                if this_order.deposit_paid:
                    this_order.final_paid = True
                    this_order.save()
                    return redirect(reverse('profile'))
                else:
                    this_order.deposit_paid = True
                    this_order.save()
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
