from django.urls import path
from .views import payment, summary, user_invoice


urlpatterns = [
    path('payment/<slug>', payment, name="payment"),
    path('summary/<slug>', summary, name="summary"),
    path('invoice/<slug>', user_invoice, name="invoice")
]
