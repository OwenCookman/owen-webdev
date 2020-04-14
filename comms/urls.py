from django.urls import path
from comms.views import contact

urlpatterns = [
    path('contact/', contact, name="contact")
]
