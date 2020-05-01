from django.urls import path
from .views import payment, summary


urlpatterns = [
    path('payment/<slug>', payment, name="payment"),
    path('summary/<slug>', summary, name="summary")
]
